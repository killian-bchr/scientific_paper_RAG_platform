from typing import Dict

import requests

from backend.core.config import Config
from backend.models import OpenAlexData


class MetadataLoader:
    @staticmethod
    def clean_doi(doi: str) -> str:
        doi = doi.lower().strip()
        doi = doi.replace("https://doi.org/", "")
        doi = doi.replace("http://doi.org/", "")

        return doi

    # TODO: Define all extractots functions

    @staticmethod
    def build_open_alex_data(data: Dict) -> OpenAlexData:
        return OpenAlexData(
            title=data.get("title"),
            doi=data.get("doi"),
            publication_year=int(data.get("publication_year")),
            type=data.get("type"),
            is_open_access=data.get("open_access", {}).get("is_oa"),
            primary_topic=data.get("primary_topic", {}).get("display_name"),
            journal=data.get("primary_location", {})
            .get("source", {})
            .get("display_name"),
            publisher=data.get("primary_location", {})
            .get("source", {})
            .get("host_organization_name"),
            cited_by_count=int(data.get("cited_by_count")),
            fwci=float(data.get("fwci")),
            citation_normalized_percentile=float(
                data.get("citation_normalized_percentile", {}).get("value")
            ),
        )

    @staticmethod
    def fetch_paper_metadata(doi: str) -> OpenAlexData:
        doi = MetadataLoader.clean_doi(doi)

        url = Config.OPEN_ALEX_URL + doi

        try:
            response = requests.get(url, timeout=10)

            if response.status_code == 200:
                data = response.json()
                result = MetadataLoader.build_open_alex_data(data)
                return result

            elif response.status_code == 404:
                print("DOI not found in OpenAlex.")
                return None

            else:
                print(f"Error: {response.status_code}")
                return None

        except requests.RequestException as e:
            print(f"Request failed: {e}")
            return None
