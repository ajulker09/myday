
import os

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError(
        "OPENAI_API_KEY is missing. Add it to the repository's .env file."
    )

client = OpenAI(api_key=api_key)


def get_openai_client() -> OpenAI:
    """Return the configured OpenAI client."""
    return client
