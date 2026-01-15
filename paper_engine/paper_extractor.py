from pathlib import Path
from typing import Dict

from docling.datamodel.document import ConversionResult
from docling.document_converter import DocumentConverter
from huggingface_hub import hf_hub_download

from config import Config
from exceptions import InvalidPDFFormatError, PDFConversionError, PDFNotFoundError


class PaperExtractor:
    def __init__(self):
        self.converter = DocumentConverter()

        hf_hub_download(
            repo_id="docling-project/docling-layout-heron",
            filename="config.json",
            local_dir="./models/docling-layout-heron",
            local_dir_use_symlinks=False,
        )

    def _is_valid_pdf(self, filepath: Path) -> bool:
        try:
            if filepath.suffix.lower() != ".pdf":
                return False

            if filepath.stat().st_size == 0:
                return False

            return True

        except OSError:
            return False

    def convert_paper(self, paper_name: str) -> ConversionResult:
        if not paper_name.endswith(".pdf"):
            paper_name = paper_name + ".pdf"

        filepath = Path(Config.PDF_FOLDER_PATH) / paper_name

        if not filepath.exists():
            raise PDFNotFoundError(f"PDF Article not found : {filepath}")

        if not self._is_valid_pdf(filepath):
            raise InvalidPDFFormatError(f"Fichier invalide ou corrompu : {filepath}")

        try:
            result = self.converter.convert(filepath)
            return result

        except FileNotFoundError as e:
            raise PDFNotFoundError(
                f"File has disappeared during the conversion : {filepath}"
            ) from e

        except PermissionError as e:
            raise PDFConversionError(
                f"Insufficient permissions to read : {filepath}"
            ) from e

        except (ValueError, RuntimeError) as e:
            raise InvalidPDFFormatError(
                f"Conversion of the PDF file has failed : {str(e)[:200]}"
            ) from e

        except Exception as e:
            raise PDFConversionError(
                f"Unexpected error during the conversion : {type(e).__name__}: {e}"
            ) from e

    def extract_body(self, doc: ConversionResult) -> Dict:
        dump = doc.model_dump()

        assembled = dump.get("assembled")
        if not assembled:
            raise ValueError("'assembled' not in doc")

        body = assembled.get("body")
        if not body:
            raise ValueError("'body' not in doc")

        return body

    def extract_paper_content(self, paper_name: str) -> Dict:
        doc = self.convert_paper(paper_name)
        return self.extract_body(doc)
