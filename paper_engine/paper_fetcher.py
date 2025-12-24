import arxiv
from arxiv import Search, SortCriterion, Result
from typing import Dict, List, Optional

from exceptions import InvalidSearchParametersError, MissingSearchParameterError, PaperNotFound


class PaperFetcher:
    def __init__(self):
        self.client = arxiv.Client()

    def build_params(
        self,
        max_results: int,
        sort_by: SortCriterion,
        **additional_params,
    ) -> Dict:
        params = {
            'max_results': max_results,
            **additional_params,
        }

        if sort_by:
            params['sort_by'] = sort_by

        return params

    def create_search(
        self,
        max_results: int = 3,
        sort_by: Optional[SortCriterion] = None,
        **additional_params,
    ) -> Search:
        id_list = additional_params.get('id_list', None)
        query = additional_params.get('query', None)

        if id_list and query:
            raise InvalidSearchParametersError("You should not use 'id_list' and 'query' together !")

        if not id_list and not query:
            raise MissingSearchParameterError("You have to input at least 'id_list' or 'query' !")

        params = self.build_params(max_results, sort_by, **additional_params)
        return Search(**params)

    def search_by_category(
        self,
        category: str,
        max_results: int = 3,
        sort_by: SortCriterion = SortCriterion.SubmittedDate,
    ) -> Search:
        params = {'query': f"{category}"}
        return self.create_search(
            max_results=max_results,
            sort_by=sort_by,
            **params,
        )

    def search_by_ids(
        self,
        id_list: List[str],
        sort_by: SortCriterion = SortCriterion.SubmittedDate,
    ) -> Search:
        params = {'id_list': id_list}
        max_results = len(id_list)

        return self.create_search(
            max_results=max_results,
            sort_by=sort_by,
            **params,
        )

    def execute_search(self, search: Search) -> List[Result]:
        return list(self.client.results(search))

    def fetch_papers_by_query(
        self,
        query: str,
        max_results: int = 3,
        **kwargs
    ) -> List[Result]:
        search = self.create_search(
            query=query,
            max_results=max_results,
            **kwargs
        )
        return self.execute_search(search)

    def fetch_papers_by_ids(
        self,
        id_list: List[str],
        **kwargs,
    ) -> List[Result]:
        search = self.search_by_ids(id_list, **kwargs)
        return self.execute_search(search)

    def fetch_paper_by_id(self, paper_id: str, **kwargs) -> Result:
        results = self.fetch_papers_by_ids([paper_id], **kwargs)
        if results is None or len(results) == 0:
            raise PaperNotFound(f"Paper not found with following id : {paper_id}")

        return results[0]
