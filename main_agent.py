import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, AgentType
from tools.google_places_tool import search_restaurants

load_dotenv()

llm = ChatOpenAI(
    temperature=0,
    model="gpt-4",  # or gpt-4o when allowed
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

tools = [search_restaurants]

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)
