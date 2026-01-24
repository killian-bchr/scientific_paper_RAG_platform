import os

from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer

from backend.core.exceptions import MissingEnvironmentVariableError

load_dotenv("config.env")


class Config:
    @staticmethod
    def get_env_variable(name: str) -> str:
        """
        Retrieve the value of an environment variable.

        Args:
            name: The name of the environment variable to retrieve.

        Returns:
            str: The value of the environment variable.

        Raises:
            MissingEnvironmentVariableError: If the environment variable is missing.
        """
        value = os.getenv(name)
        if value is None:
            raise MissingEnvironmentVariableError(
                f"Missing environment variable: {name}"
            )
        return value

    PDF_FOLDER_PATH = get_env_variable("PDF_FOLDER_PATH")
    EMBEDDING_MODEL = SentenceTransformer("all-MiniLM-L6-v2")
    DATABASE_URL = get_env_variable("DATABASE_URL")
    SECRET_KEY = get_env_variable("SECRET_KEY")
    ALGORITHM = get_env_variable("ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES = int(get_env_variable("ACCESS_TOKEN_EXPIRE_MINUTES"))
