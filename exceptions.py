class MissingEnvironmentVariableError(Exception):
    """Raised when an expected environment variable is missing."""
    pass


class DownloadingPDFError(Exception):
    """Raised when an error occurs during PDF download."""
    pass


class PDFConversionError(Exception):
    """Raised when an error occurs during the conversion of a PDF file."""
    pass


class PDFNotFoundError(Exception):
    """Raised when PDF file is not found."""
    pass


class InvalidPDFFormatError(Exception):
    """Raised when PDF format is invalid or corrupted."""
    pass


class ArxivSearchError(Exception):
    """Base exception for arXiv search errors."""
    pass


class InvalidSearchParametersError(ArxivSearchError):
    """Raised when search parameters are invalid or conflicting."""
    pass


class MissingSearchParameterError(ArxivSearchError):
    """Raised when required search parameters are missing."""
    pass


class PaperNotFound(ArxivSearchError):
    """Raised when a paper with a specific arXiv id not found."""
    pass


class InvalidDate(Exception):
    """Raised when a date is invalid and impossible to parse."""
    pass
