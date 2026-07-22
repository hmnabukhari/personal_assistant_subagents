import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from config import MODEL_NAME, TEMPERATURE

load_dotenv()

llm = ChatOpenAI(
    model=MODEL_NAME,
    temperature=TEMPERATURE,
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
     max_tokens=1000, 
)
print("LLM:", llm)
print("max_tokens:", llm.max_tokens)