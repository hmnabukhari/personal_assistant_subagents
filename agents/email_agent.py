from langchain.agents import create_agent

from utils.llm import llm
from tools.email_tools import send_email
from prompts.email_prompt import EMAIL_PROMPT


email_agent = create_agent(
    model=llm,
    tools=[send_email],
    system_prompt=EMAIL_PROMPT,
)