from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # These will look for matching keys in your .env file
    secret_key: str
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    # This config tells Pydantic to read from a .env file
    model_config = SettingsConfigDict(env_file=".env")


# Create a single instance to use throughout your app
settings = Settings()
