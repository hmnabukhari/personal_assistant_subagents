from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Load variables from .env
load_dotenv()

# Create the LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    temperature=0
)