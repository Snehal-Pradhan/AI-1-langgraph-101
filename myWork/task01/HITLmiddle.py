import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from utils.models import model
from langchain.agents.middleware import AgentMiddleware, AgentState
from langchain.agents import create_agent
from langchain_core.tools import tool
from langgraph.types import interrupt, Command
from langgraph.checkpoint.memory import MemorySaver
from langchain_core.messages import HumanMessage
from langsmith import uuid7
from typing import Any


@tool
def delete_database(database_name: str) -> str:
    """Delete a database. THIS IS DANGEROUS!"""

    response = interrupt({
        "action": "delete_database",
        "database_name": database_name,
        "warning": "This will permanently delete the database!",
        "message": "Are you absolutely sure?"
    })

    if response.get("confirmed"):
        return f"Database '{database_name}' has been deleted (simulation)"
    else:
        return "Database deletion cancelled"


class SafetyMiddleware(AgentMiddleware):
    name = "safety_checker"

    def after_model(self, state: AgentState) -> dict[str, Any] | None:
        last_message = state["messages"][-1]

        if hasattr(last_message, 'tool_calls') and last_message.tool_calls:
            for tool_call in last_message.tool_calls:
                if "delete" in tool_call["name"].lower():
                    print("   [SAFETY] Dangerous operation detected!")
                    print(f"   Tool: {tool_call['name']}")
                    print(f"   Args: {tool_call['args']}")

        return None


production_agent = create_agent(
    model=model,
    tools=[delete_database],
    middleware=[SafetyMiddleware()],
    checkpointer=MemorySaver()
)

config_4 = {"configurable": {"thread_id": uuid7()}}

print("\n" + "=" * 50)
print("DANGEROUS OPERATION ATTEMPT")
print("=" * 50 + "\n")

result = production_agent.invoke(
    {
        "messages": [HumanMessage(content="Delete the production_db database")]
    },
    config=config_4
)

if "__interrupt__" in result:
    interrupt_info = result["__interrupt__"][0]
    print("\n  Human approval required:")
    print(f"   {interrupt_info.value['warning']}")
    print(f"   Database: {interrupt_info.value['database_name']}")

print("\n(In a real app, a human would review this before proceeding)")
