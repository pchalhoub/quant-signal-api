import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    ALPHA_VANTAGE_API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")
    DATABASE_URL = os.getenv("DATABASE_URL")
    ENV = os.getenv("ENV", "dev")

settings = Settings()