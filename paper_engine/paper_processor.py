import logging
from datetime import date
from typing import Dict, List, Optional, Tuple

from arxiv import Result
from numpy import ndarray

from config import Config
from exceptions import DownloadingPDFError
from settings.arxiv_categories import ARXIV_CATEGORIES
from settings.constants import Category, DefaultCategories, Domains, Names

logger = logging.getLogger(__name__)


class PaperProcessor:
    @staticmethod
    def extract_title(paper: Result) -> str:
        return paper.title

    @staticmethod
    def extract_pdf_url(paper: Result) -> str:
        return paper.pdf_url

    @staticmethod
    def extract_abstract(paper: Result) -> str:
        return paper.summary

    @staticmethod
    def extract_publication_date(paper: Result) -> date:
        return paper.published.date()

    @staticmethod
    def parse_arxiv_categories(
        category_codes: List[str],
    ) -> List[Tuple[Domains, Category]]:
        categorized = []
        unknown_categories = set()

        for code in category_codes:
            category_info = ARXIV_CATEGORIES.get(code)
            if category_info is None:
                unknown_categories.add(code)
                categorized.append((Domains.OTHER, DefaultCategories.OTHER))
                continue

            domain = category_info.get(Names.DOMAIN, Domains.OTHER)
            category_name = category_info.get(Names.CATEGORY, DefaultCategories.OTHER)
            categorized.append((domain, category_name))

        if unknown_categories:
            logger.warning(f"Unknown ArXiv Categories : {unknown_categories}")

        return categorized

    @staticmethod
    def extract_category_info(paper: Result) -> List[Tuple[Domains, Category]]:
        return PaperProcessor.parse_arxiv_categories(paper.categories)

    @staticmethod
    def extract_domains(paper: Result) -> List[Domains]:
        category_info = PaperProcessor.extract_category_info(paper)
        return [cat[0] for cat in category_info]

    @staticmethod
    def extract_categories(paper: Result) -> List[Category]:
        category_info = PaperProcessor.extract_category_info(paper)
        return [cat[1] for cat in category_info]

    @staticmethod
    def extract_authors(paper: Result) -> List[Result.Author]:
        return paper.authors

    @staticmethod
    def extract_authors_names(paper: Result) -> List[str]:
        return [a.name for a in paper.authors]

    @staticmethod
    def extract_arxiv_id(paper: Result) -> str:
        return paper.get_short_id().split("v")[0]

    @staticmethod
    def download_paper(paper: Result, filename: Optional[str] = None) -> None:
        if filename is None:
            paper_id = paper.get_short_id().split("v")[0]
            filename = f"{paper_id.replace('/', '_')}.pdf"
        elif not filename.endswith(".pdf"):
            filename += ".pdf"

        try:
            paper.download_pdf(dirpath=Config.PDF_FOLDER_PATH, filename=filename)
            logger.info("PDF successfully downloaded !")

        except Exception:
            raise DownloadingPDFError("Error during the downloading of the PDF !")

    @staticmethod
    def create_chunks(doc_body: Dict) -> List[Dict]:
        chunks = []

        for item in doc_body:
            label = item.get("label")
            text = item.get("text", "")
            if not text:
                continue

            chunk = {
                "chunk_type": label.value if hasattr(label, "value") else str(label),
                "page_no": int(item.get("page_no")),
                "content": text.strip(),
            }

            chunks.append(chunk)

        return chunks

    @staticmethod
    def split_chunks(
        chunks: List[Dict], max_chars: int = 300, overlap: int = 50
    ) -> List[Dict]:
        new_chunks = []

        for chunk in chunks:
            text = chunk.get("content")
            if not text:
                continue

            if len(text) <= max_chars:
                new_chunks.append(chunk)
                continue

            start = 0
            while start < len(text):
                end = start + max_chars
                sub_text = text[start:end]

                new_chunks.append(
                    {
                        **chunk,
                        "content": sub_text,
                    }
                )

                start = end - overlap

        return new_chunks

    @staticmethod
    def extract_chunk_texts(chunks: List[Dict]) -> List[str]:
        return [chunk["content"] for chunk in chunks]

    @staticmethod
    def embed_texts(raw_text: List[str]) -> ndarray:
        model = Config.EMBEDDING_MODEL
        return model.encode(raw_text, normalize_embeddings=True)

    @staticmethod
    def create_embeddings(chunks: List[Dict]) -> ndarray:
        text = PaperProcessor.extract_chunk_texts(chunks)
        return PaperProcessor.embed_texts(text)

    @staticmethod
    def attach_embeddings_to_chunks(
        chunks: List[Dict],
        embeddings: ndarray,
    ) -> List[Dict]:
        if len(chunks) != len(embeddings):
            raise ValueError("Chunks and embeddings must have the same length")

        new_chunks = []
        for chunk, embedding in zip(chunks, embeddings):
            new_chunks.append({**chunk, "embedding": embedding})

        return new_chunks

    @staticmethod
    def create_chunks_with_embeddings(doc_body: Dict) -> List[Dict]:
        raw_chunks = PaperProcessor.create_chunks(doc_body)
        cleaned_chunks = PaperProcessor.split_chunks(raw_chunks)
        embeddings = PaperProcessor.create_embeddings(cleaned_chunks)

        return PaperProcessor.attach_embeddings_to_chunks(cleaned_chunks, embeddings)

    @staticmethod
    def extract_type_from_chunk(chunk: Dict) -> str:
        chunk_type = chunk.get("chunk_type")
        if not chunk_type:
            raise ValueError("Chunk should have a 'chunk_type' !")

        return chunk_type

    @staticmethod
    def extract_page_no_from_chunk(chunk: Dict) -> int:
        page_no = chunk.get("page_no")
        if page_no is None:
            raise ValueError("Chunk should have a 'page_no' !")

        return page_no

    @staticmethod
    def extract_content_from_chunk(chunk: Dict) -> str:
        content = chunk.get("content")
        if content is None:
            raise ValueError("Chunk should have any content !")

        return content

    @staticmethod
    def extract_embedding_from_chunk(chunk: Dict) -> ndarray:
        embedding = chunk.get("embedding")
        if embedding is None:
            raise ValueError("Chunk should have an embedding related to its content !")

        return embedding
