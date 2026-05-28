import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from utils.models import model
from tools import get_weather, search_movies
from langchain.agents import create_agent
from langgraph.checkpoint.memory import MemorySaver
from langsmith import uuid7

checkpointer = MemorySaver()

agent_with_memory = create_agent(
    model=model,
    tools=[get_weather, search_movies],
    system_prompt="You are a helpful assistant.",
    checkpointer=checkpointer
)

config = {"configurable": {"thread_id": uuid7()}}

result1 = agent_with_memory.invoke(
    {"messages": [{"role": "user", "content": "My name is Alice and I love sci-fi movies."}]},
    config=config
)
print("Response 1:", result1["messages"][-1].content)

result2 = agent_with_memory.invoke(
    {"messages": [{"role": "user", "content": "What's my name and what movies do I like?"}]},
    config=config
)
print("\nResponse 2:", result2["messages"][-1].content)

new_config = {"configurable": {"thread_id": uuid7()}}

result3 = agent_with_memory.invoke(
    {"messages": [{"role": "user", "content": "What's my name?"}]},
    config=new_config
)
print("New thread response:", result3["messages"][-1].content)
