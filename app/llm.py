import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from app.tools import (
    create_it_ticket,
    check_ticket_status,
    calculate_expense,
    search_knowledge_base,
)


load_dotenv()

llm = ChatOpenAI(
    model="openrouter/free",
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

llm_with_tools = llm.bind_tools(
    [
        create_it_ticket,
        check_ticket_status,
        calculate_expense,
        search_knowledge_base,
    ]
)