from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from config import MODEL_NAME, TEMPERATURE
# Load variables from .env
load_dotenv()

# Create the LLM
llm = ChatGoogleGenerativeAI(
    model=MODEL_NAME,
    temperature=TEMPERATURE
)