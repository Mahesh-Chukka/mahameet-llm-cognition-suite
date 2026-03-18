from openai import OpenAI
import instructor
from .config import settings

_client = OpenAI(api_key=settings.OPENAI_API_KEY)
llm = instructor.from_openai(_client)