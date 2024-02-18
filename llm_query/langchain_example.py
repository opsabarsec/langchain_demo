from langchain_openai.chat_models import ChatOpenAI
from dotenv import load_dotenv
from pathlib import Path
import os

dotenv_path = Path('./.env')
load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
chat_model = ChatOpenAI(openai_api_key=api_key)


class Pred:
    """Get the answer from LLM"""
    global chat_model

    def __init__(self):
        self.chat_model = chat_model

    def answer(self, my_txt) -> str:
        return self.chat_model.invoke(str(my_txt))
