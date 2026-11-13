"""Environment-based application settings."""

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application configuration loaded from environment variables or .env."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    app_name: str = "Dotin Backend"
    debug: bool = False
    database_host: str = "localhost"
    database_port: int = 5432
    database_name: str = "dotin_db"
    database_user: str = "dotin_user"
    database_password: SecretStr
