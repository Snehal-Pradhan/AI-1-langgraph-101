import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from utils.models import model
from tools import get_weather, search_movies
from langchain.agents import create_agent

agent = create_agent(
    model=model,
    tools=[get_weather, search_movies],
    system_prompt="You are a helpful assistant."
)

print("Streaming agent steps:\n")
for chunk in agent.stream(
    {"messages": [{"role": "user", "content": "What's the weather in Boston? (42.36° N, 71.06° W)"}]},
    stream_mode="updates"
):
    for node_name, data in chunk.items():
        print(f"Step: {node_name}")
        if "messages" in data:
            message = data["messages"][-1]
            if hasattr(message, 'tool_calls') and message.tool_calls:
                print(f"   Tool call: {message.tool_calls[0]['name']}")
            elif hasattr(message, 'content'):
                c = message.content
                print(f"   Content: {c[:100]}..." if len(c) > 100 else f"   Content: {c}")
        print()

print("Streaming tokens:\n")
for token, metadata in agent.stream(
    {"messages": [{"role": "user", "content": "Tell me about LangGraph in one sentence."}]},
    stream_mode="messages"
):
    if metadata.get('langgraph_node') == 'model':
        for block in token.content_blocks:
            if block.get('type') == 'text' and block.get('text'):
                print(block['text'], end='', flush=True)
print("\n")
