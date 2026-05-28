import sys
from pathlib import Path
import warnings

project_root = Path(__file__).resolve().parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from utils.models import model
from tools import get_weather, search_movies
from typing_extensions import TypedDict
from typing import Annotated, List
from langgraph.graph.message import AnyMessage, add_messages
from langgraph.prebuilt import ToolNode
from langgraph.graph import StateGraph, START, END
from langchain_core.messages import SystemMessage, HumanMessage

warnings.filterwarnings('ignore', message='LangSmith now uses UUID v7')


class State(TypedDict):
    messages: Annotated[List[AnyMessage], add_messages]


tools = [search_movies, get_weather]
model_with_tools = model.bind_tools(tools)
tool_node = ToolNode(tools)


def assistant(state: State):
    system_prompt = "You are a helpful assistant that can check weather and recommend movies."
    all_messages = [SystemMessage(system_prompt)] + state["messages"]
    response = model_with_tools.invoke(all_messages)
    return {"messages": [response]}


def should_continue(state: State):
    messages = state["messages"]
    last_message = messages[-1]
    if last_message.tool_calls:
        return "continue"
    else:
        return "end"


builder = StateGraph(State)

builder.add_node("assistant", assistant)
builder.add_node("tool_node", tool_node)

builder.add_edge(START, "assistant")

builder.add_conditional_edges(
    "assistant",
    should_continue,
    {
        "continue": "tool_node",
        "end": END,
    },
)

builder.add_edge("tool_node", "assistant")

agent = builder.compile(name="agent")

question = "What is the weather in SF today (37.77° N, 122.42° W), and what are some good Sci-Fi movies?"

result = agent.invoke({"messages": HumanMessage(content=question)})

for message in result["messages"]:
    message.pretty_print()
