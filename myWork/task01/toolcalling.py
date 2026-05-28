import sys
from pathlib import Path
import warnings

project_root = Path(__file__).resolve().parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from utils.models import model
from tools import get_weather, search_movies

warnings.filterwarnings('ignore', message='LangSmith now uses UUID v7')

tools = [get_weather, search_movies]
model_with_tools = model.bind_tools(tools)

message = "What's the weather like in Seattle? (Seattle's coordinates are approximately 47.6° N latitude and 122.33° W longitude)"

response = model_with_tools.invoke(message)

print("Tool calls:", response.tool_calls)
