from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import AnyHttpUrl


class Settings(BaseSettings):
    """
    Application configuration.

    Values can come from:
    1. MCP client enviroment variables, which are passed to the MCP server
    2. local .env file for development only
    """
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )
    
    arcgis_portal_url: AnyHttpUrl
    orgid: str

settings = Settings() #singleton instance