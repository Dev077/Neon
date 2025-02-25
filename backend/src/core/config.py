from pydantic_settings import BaseSettings #for managing application settings and configuration in a structured way
from typing import Optional # for type enforcement
from functools import lru_cache # for caching the settings

class Settings(BaseSettings):
    #App Settings
    APPNAME: str = "Neon"
    DEBUG : bool = True

    #API Settings
    API_VERSION: str = "v1"
    HOST: str = "0.0.0.0"
    PORT: int = 8000

    #WebsSockets Settings
    WE_MESSAGE_QUEUE_SIZE: int  = 100

    #VoiceParsing
    VOICE_SAMPLE_RATE: int = 16000

    class Config:
        case_sensitive = True
        env_file = ".env"

@lru_cache() # Prevents multiple reads of environment files and improve performance
def get_settings():
    return Settings()


