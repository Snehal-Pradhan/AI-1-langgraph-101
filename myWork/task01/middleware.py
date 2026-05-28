import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from utils.models import model
from langchain.agents.middleware import dynamic_prompt, ModelRequest
from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
from typing import TypedDict


class Context(TypedDict):
    user_role: str


@dynamic_prompt
def dynamic_prompt_middleware(request: ModelRequest) -> str:
    user_role = request.runtime.context.get("user_role", "general")

    if user_role == "expert":
        return "You are an AI assistant for experts. Provide detailed technical responses with code examples."
    elif user_role == "beginner":
        return "You are an AI assistant for beginners. Explain concepts simply, avoid jargon."
    else:
        return "You are a helpful AI assistant."


@tool
def explain_concept(concept: str) -> str:
    """Explain a programming concept."""
    explanations = {
        "async": "Asynchronous programming allows code to run without blocking.",
        "recursion": "Recursion is when a function calls itself."
    }
    return explanations.get(concept.lower(), "Concept not found.")


agent_with_middleware = create_agent(
    model=model,
    tools=[explain_concept],
    middleware=[dynamic_prompt_middleware],
    context_schema=Context
)

print("=" * 50)
print("EXPERT USER")
print("=" * 50)
result = agent_with_middleware.invoke(
    {"messages": [HumanMessage(content="Explain async programming")]},
    context={"user_role": "expert"}
)
print(result["messages"][-1].content)
print()

print("=" * 50)
print("BEGINNER USER")
print("=" * 50)
result = agent_with_middleware.invoke(
    {"messages": [HumanMessage(content="Explain async programming")]},
    context={"user_role": "beginner"}
)
print(result["messages"][-1].content)
