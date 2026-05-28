import sys
from pathlib import Path
import warnings

project_root = Path(__file__).resolve().parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from utils.models import model
from tools import get_weather, search_movies
from langchain_core.messages import HumanMessage, ToolMessage

warnings.filterwarnings('ignore', message='LangSmith now uses UUID v7')

tools = [get_weather, search_movies]
model_with_tools = model.bind_tools(tools)

message = "What's the weather like in Seattle? (Seattle's coordinates are approximately 47.6° N latitude and 122.33° W longitude)"

response = model_with_tools.invoke(message)

if response.tool_calls:
    tool_call = response.tool_calls[0]

    if tool_call["name"] == "get_weather":
        result = get_weather.invoke(tool_call["args"])
    elif tool_call["name"] == "search_movies":
        result = search_movies.invoke(tool_call["args"])

    tool_message = ToolMessage(
        content=result,
        tool_call_id=tool_call["id"]
    )

    final_response = model_with_tools.invoke([
        HumanMessage(content=message),
        response,
        tool_message
    ])

    final_response.pretty_print()
