"""
PREVIOUS BUG (first attempt):

Used `from langgraph.prebuilt import create_react_agent` with `state_modifier=`.
That was the OLD API — deprecated in LangGraph V1.0.

The NEW API uses `from langchain.agents import create_agent` with `system_prompt=`.
Key differences:
  - Old: create_react_agent(model, tools, state_modifier="...")
  - New: create_agent(model, tools, system_prompt="...")
"""

import sys
from pathlib import Path
import warnings

project_root = Path(__file__).resolve().parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from utils.models import model
from tools import get_weather, search_movies
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage

warnings.filterwarnings('ignore', message='LangSmith now uses UUID v7')

agent = create_agent(
    model=model,
    tools=[get_weather, search_movies],
    system_prompt="You are a helpful assistant that can check weather and recommend movies."
)

result = agent.invoke({
    "messages": [HumanMessage(content="What's the weather in NYC? (40.71° N, 74.01° W) Also recommend some sci-fi movies.")]
})

for message in result["messages"]:
    message.pretty_print()
