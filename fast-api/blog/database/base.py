from blog.core.config import Settings
from functools import lru_cache
from sqlalchemy.orm import declarative_base


@lru_cache
def get_settings() -> Settings:
    return Settings(env_file='.env')


Base = declarative_base()

settings: Settings = get_settings()
