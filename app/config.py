from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    GEMINI_API_KEY: str 
    DATABASE_URL: str = "sqlite:///./ecommerce.db"
    MODEL_NAME: str = "gemini-pro"  # Using stable gemini-pro model
    
    class Config:
        env_file = ".env"

def get_settings():
    return Settings()  # Removed lru_cache to allow config updates