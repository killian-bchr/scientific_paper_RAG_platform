from sqlalchemy.orm import Session

from crud import CRUD
from paper_engine import PaperBuilder, PaperExtractor, PaperFetcher, PaperProcessor


class Pipeline:
    def __init__(self, paper_id: str, session: Session):
        self.paper_id = paper_id
        self.session = session
        self.paper_extractor = PaperExtractor()
        self.paper_fetcher = PaperFetcher()

    def run_pipeline(self):
        # Extract
        raw_paper = self.paper_fetcher.fetch_paper_by_id(self.paper_id)
        PaperProcessor.download_paper(raw_paper)
        raw_doc = self.paper_extractor.extract_paper_content(self.paper_id)

        # Transform
        raw_chunks = PaperProcessor.create_chunks_with_embeddings(raw_doc)
        paper = PaperBuilder.build_paper(raw_paper)
        chunks = PaperBuilder.build_chunks(raw_chunks)

        # Load
        paper_orm = CRUD.paper_to_orm(self.session, paper, flush=True)
        CRUD.chunks_to_orm(self.session, chunks, paper_orm)

        self.session.commit()
