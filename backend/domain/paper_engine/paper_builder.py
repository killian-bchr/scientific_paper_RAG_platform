from typing import Dict, List

from arxiv import Result
from models import Author, Category, Chunk, Domain, Paper
from paper_engine.paper_processor import PaperProcessor


class PaperBuilder:
    @staticmethod
    def build_author(author: Result.Author) -> Author:
        return Author(name=author.name)

    @staticmethod
    def build_authors(authors: List[Result.Author]) -> List[Author]:
        return [PaperBuilder.build_author(a) for a in authors]

    @staticmethod
    def build_domain(domain: str) -> Domain:
        return Domain(name=domain)

    @staticmethod
    def build_domains(domains: List[str]) -> List[Domain]:
        return [PaperBuilder.build_domain(d) for d in domains]

    @staticmethod
    def build_category(category: str, domain: str) -> Category:
        return Category(name=category, domain=PaperBuilder.build_domain(domain))

    @staticmethod
    def build_categories(categories: List[str], domains: List[str]) -> List[Category]:
        return [PaperBuilder.build_category(c, d) for c, d in zip(categories, domains)]

    @staticmethod
    def build_paper(paper: Result) -> Paper:
        authors = PaperProcessor.extract_authors(paper)
        domains = PaperProcessor.extract_domains(paper)
        categories = PaperProcessor.extract_categories(paper)

        return Paper(
            arxiv_id=PaperProcessor.extract_arxiv_id(paper),
            title=PaperProcessor.extract_title(paper),
            pdf_url=PaperProcessor.extract_pdf_url(paper),
            abstract=PaperProcessor.extract_abstract(paper),
            publication_date=PaperProcessor.extract_publication_date(paper),
            authors=PaperBuilder.build_authors(authors),
            domains=PaperBuilder.build_domains(domains),
            categories=PaperBuilder.build_categories(categories, domains),
        )

    @staticmethod
    def build_papers(papers: List[Result]) -> List[Paper]:
        return [PaperBuilder.build_paper(p) for p in papers]

    @staticmethod
    def build_chunk(chunk: Dict) -> Chunk:
        return Chunk(
            chunk_type=PaperProcessor.extract_type_from_chunk(chunk),
            page_no=PaperProcessor.extract_page_no_from_chunk(chunk),
            content=PaperProcessor.extract_content_from_chunk(chunk),
            embedding=PaperProcessor.extract_embedding_from_chunk(chunk),
        )

    @staticmethod
    def build_chunks(chunks: List[Dict]) -> List[Chunk]:
        return [PaperBuilder.build_chunk(c) for c in chunks]
