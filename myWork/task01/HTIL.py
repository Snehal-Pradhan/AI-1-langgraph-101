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
def send_email(to: str, subject: str, body: str) -> str:
    """Send an email to a recipient."""

    approval = interrupt({
        "action": "send_email",
        "to": to,
        "subject": subject,
        "body": body,
        "message": "Do you want to send this email?"
    })

    if approval.get("approved"):
        return f"Email sent to {to} with subject '{subject}'"
    else:
        return "Email cancelled by user"


print("Tool created successfully!")
print(f"Tool name: {send_email.name}")
print(f"Tool description: {send_email.description}\n")

checkpointer = MemorySaver()

agent = create_agent(
    model=model,
    tools=[send_email],
    system_prompt="You are a helpful email assistant. When asked to send emails, use the send_email tool.",
    checkpointer=checkpointer
)

config = {"configurable": {"thread_id": uuid7()}}

result = agent.invoke(
    {
        "messages": [HumanMessage(content="Send an email to alice@example.com with subject 'Meeting Tomorrow' and body 'Let's meet at 3pm.'")]
    },
    config=config
)

if "__interrupt__" in result:
    print("Agent paused for approval\n")

    interrupt_info = result["__interrupt__"][0]

    print("Interrupt details:")
    print(f"  To: {interrupt_info.value['to']}")
    print(f"  Subject: {interrupt_info.value['subject']}")
    print(f"  Body: {interrupt_info.value['body']}")
    print(f"  Message: {interrupt_info.value['message']}\n")
else:
    print("Agent completed without interrupt\n")

result = agent.invoke(
    Command(resume={"approved": True}),
    config=config
)

print("Final response:")
print(result["messages"][-1].content)

print("\n" + "=" * 50)
print("REJECTION EXAMPLE")
print("=" * 50 + "\n")

config_2 = {"configurable": {"thread_id": uuid7()}}

result = agent.invoke(
    {
        "messages": [HumanMessage(content="Send an email to bob@example.com with subject 'Greeting' and body 'Hello!'")]
    },
    config=config_2
)

result = agent.invoke(
    Command(resume={"approved": False}),
    config=config_2
)

print("Final response:")
print(result["messages"][-1].content)
