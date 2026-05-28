import sys
from pathlib import Path
import warnings

project_root = Path(__file__).resolve().parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from utils.models import model
from langchain_core.messages import SystemMessage, HumanMessage

warnings.filterwarnings('ignore', message='LangSmith now uses UUID v7')

messages = [
    SystemMessage(content="You are a pokemon trainer in the pokemon world"),
    HumanMessage(content="why are we making pokemons for our entertainment"),
]

response = model.invoke(messages)
response.pretty_print()

messages.append(response)
messages.append(HumanMessage(
    content="i know we dont make them and they are found naturally, "
            "but as a trainer we make them fight without asking their permissions "
            "and they take the damages for our ego, when we lose they need treatment "
            "in pokemon center not us. how is that fair, they are fighting and the "
            "trainer is getting rich and wealthy and earn badges but the pokemon just "
            "becomes a fighting machine which lives a similar life what it would have "
            "lived in wild"
))

second_response = model.invoke(messages)
second_response.pretty_print()
