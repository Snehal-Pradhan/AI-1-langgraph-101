import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from utils.models import model
from langgraph.types import interrupt, Command
from langchain_core.tools import tool
from langchain.agents import create_agent
from langgraph.checkpoint.memory import MemorySaver
from langchain_core.messages import HumanMessage
from langsmith import uuid7


@tool
def send_email_v2(to: str, subject: str, body: str) -> str:
    """Send an email to a recipient."""

    response = interrupt({
        "action": "send_email",
        "to": to,
        "subject": subject,
        "body": body,
        "message": "Review this email. You can approve, reject, or edit it."
    })

    if response["type"] == "approve":
        return f"Email sent to {to} with subject '{subject}'"
    elif response["type"] == "reject":
        return "Email cancelled"
    elif response["type"] == "edit":
        to = response.get("to", to)
        subject = response.get("subject", subject)
        body = response.get("body", body)
        return f"""Email sent with edits:
                To: {to}
                Subject: {subject}
                Body: {body}"""

    return "Unknown response"


agent_v2 = create_agent(
    model=model,
    tools=[send_email_v2],
    system_prompt="You are a helpful email assistant.",
    checkpointer=MemorySaver()
)

config_3 = {"configurable": {"thread_id": uuid7()}}

result = agent_v2.invoke(
    {
        "messages": [HumanMessage(content="Send an email to team@example.com with subject 'Team Meeting' and body 'Meeting at 3pm tomorrow.'")]
    },
    config=config_3
)

print("Paused for review...\n")

result = agent_v2.invoke(
    Command(resume={
        "type": "edit",
        "subject": "URGENT: Meeting Today at 2pm",
        "body": "This is the edited email body with more details."
    }),
    config=config_3
)

print("Final response:")
print(result["messages"][-1].content)
