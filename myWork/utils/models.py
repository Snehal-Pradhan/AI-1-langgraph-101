from dotenv import load_dotenv
load_dotenv(override=True)

from langchain.chat_models import init_chat_model

model = init_chat_model("google_genai:gemini-2.5-flash")
