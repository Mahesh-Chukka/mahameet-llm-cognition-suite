from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    OPENAI_API_KEY: str
    OPENAI_MODEL: str = "gpt-4.1-mini"
    DATABASE_URL: str = "postgresql+psycopg://postgres:postgres@localhost:5432/cognition"


settings = Settings()
