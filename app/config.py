import os
from dotenv import load_dotenv
import openai

# Load environment variables
load_dotenv()

class Settings:
    OPENAI_API_KEY: str = os.getenv("API_KEY")

# Create an instance of the settings to be reused in the app
settings = Settings()

# Set OpenAI's API key globally
openai.api_key = settings.OPENAI_API_KEY
