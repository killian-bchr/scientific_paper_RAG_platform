from collections import defaultdict
from typing import Dict, List

import numpy as np

from backend.database.tables import PaperORM
from backend.domain.retriever.base import BaseRetriever
from backend.domain.retriever.embedding_retriever import EmbeddingRetriever
from backend.domain.retriever.tfidf_retriever import TfidfRetriever
from backend.models import ChunkRanked, PaperRanked


class HybridRetriever(BaseRetriever):
    def __init__(
        self,
        papers: List[PaperORM],
        alpha: float = 0.5,
    ):
        super().__init__(papers)

        self.tfidf_retriever = TfidfRetriever(papers)
        self.embedding_retriever = EmbeddingRetriever(papers)
        self.alpha = alpha

    def aggregate_and_sort_chunks_by_paper(
        self,
        chunks: List[ChunkRanked],
    ) -> Dict[int, List[ChunkRanked]]:
        paper_chunks = defaultdict(list)

        if not chunks:
            return paper_chunks

        for chunk_ranked in chunks:
            paper_chunks[chunk_ranked.chunk.paper_id].append(chunk_ranked)

        for paper_id, chunks in paper_chunks.items():
            chunks.sort(key=lambda x: x.score, reverse=True)
            paper_chunks[paper_id] = chunks

        return paper_chunks

    def score_papers(
        self,
        papers: Dict[int, float],
        paper_chunks: Dict[int, List[ChunkRanked]],
    ) -> Dict[int, float]:
        result = {}
        for p_id, score in papers.items():
            result[p_id] = self.alpha * score

        for p_id, chunks in paper_chunks.items():
            result[p_id] += (1 - self.alpha) * float(np.mean([c.score for c in chunks]))

        return result

    def keep_top_k_papers(
        self,
        paper_scores: Dict[int, float],
        top_k: int,
    ) -> Dict[int, float]:
        papers_sorted = sorted(paper_scores.items(), key=lambda x: x[1], reverse=False)[
            :top_k
        ]

        return dict(papers_sorted)

    def build_papers_ranked(
        self,
        paper_scores: Dict[int, float],
    ) -> List[PaperRanked]:
        papers_ranked = []

        for p_id, score in paper_scores.items():
            paper = self.papers_by_id[p_id]
            paper_ranked = PaperRanked(paper=paper, score=score)
            papers_ranked.append(paper_ranked)

        return papers_ranked

    def retrieve(
        self,
        query: str,
        top_k_papers: int = 10,
        top_k_chunks: int = 5,
        chunk_relevance_threshold: float = 0.5,
    ) -> List[PaperRanked]:
        papers = self.tfidf_retriever.retrieve(query)
        chunks = self.embedding_retriever.retrieve(
            query,
            chunk_relevance_threshold,
        )

        paper_chunks = self.aggregate_and_sort_chunks_by_paper(chunks)

        paper_scores = self.score_papers(papers, paper_chunks)
        top_papers = self.keep_top_k_papers(paper_scores, top_k_papers)

        papers_ranked = self.build_papers_ranked(top_papers)

        if not chunks:
            return papers_ranked

        for paper in papers_ranked:
            relevant_chunks = paper_chunks[paper.paper.id][:top_k_chunks]
            paper.chunks = relevant_chunks

        return papers_ranked
