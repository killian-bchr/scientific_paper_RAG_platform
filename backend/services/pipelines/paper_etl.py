from arxiv import Result
from sqlalchemy.orm import Session

from backend.database.crud import CRUD
from backend.domain.paper_engine import (
    PaperBuilder,
    PaperExtractor,
    PaperFetcher,
    PaperProcessor,
)
from backend.services.pipelines.base import Pipeline


class PaperETLPipeline(Pipeline):
    def __init__(self, paper: Result, session: Session):
        self.paper = paper
        self.paper_id = PaperProcessor.extract_arxiv_id(paper)
        self.session = session
        self.paper_extractor = PaperExtractor()
        self.paper_fetcher = PaperFetcher()

    def run(self):
        # Extract
        raw_paper = self.paper_fetcher.fetch_paper_by_id(self.paper.get_short_id())
        PaperProcessor.download_paper(raw_paper)
        raw_doc = self.paper_extractor.extract_paper_content(self.paper_id)

        # Transform
        raw_chunks = PaperProcessor.create_chunks_with_embeddings(raw_doc)
        paper = PaperBuilder.build_paper(raw_paper)
        chunks = PaperBuilder.build_chunks(raw_chunks)

        # Load
        CRUD.load_complete_paper(self.session, paper, chunks)

        self.session.commit()
