import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from utils.models import model
from langchain.agents.middleware import AgentMiddleware, AgentState, ModelRequest, ModelResponse
from langchain.agents import create_agent
from langchain_core.tools import tool
from typing import Any, Callable


class RequestLoggerMiddleware(AgentMiddleware):
    def before_model(self, state: AgentState, runtime) -> dict[str, Any] | None:
        message_count = len(state.get("messages", []))
        print(f"[BEFORE MODEL] Processing {message_count} messages")
        return None

    def wrap_model_call(
        self,
        request: ModelRequest,
        handler: Callable[[ModelRequest], ModelResponse]
    ) -> ModelResponse:
        print(f"  [MODEL REQUEST]")
        print(f"   Model: {request.model if hasattr(request, 'model') else 'default'}")
        print(f"   Tools available: {len(request.tools) if request.tools else 0}")
        return handler(request)

    def after_model(self, state: AgentState, runtime) -> dict[str, Any] | None:
        last_message = state["messages"][-1]
        if hasattr(last_message, 'tool_calls') and last_message.tool_calls:
            print(f" [AFTER MODEL] Model requested {len(last_message.tool_calls)} tool call(s)")
        else:
            print(f" [AFTER MODEL] Model provided final response")
        return None


@tool
def explain_concept(concept: str) -> str:
    """Explain a programming concept."""
    explanations = {
        "async": "Asynchronous programming allows code to run without blocking.",
        "recursion": "Recursion is when a function calls itself."
    }
    return explanations.get(concept.lower(), "Concept not found.")


agent_with_logger = create_agent(
    model=model,
    tools=[explain_concept],
    middleware=[RequestLoggerMiddleware()],
)

print("\n" + "=" * 50)
print("RUNNING AGENT WITH LOGGER")
print("=" * 50 + "\n")

result = agent_with_logger.invoke({
    "messages": [{"role": "user", "content": "Explain recursion"}]
})

print("\n" + "=" * 50)
print("FINAL RESPONSE")
print("=" * 50)
print(result["messages"][-1].content)
