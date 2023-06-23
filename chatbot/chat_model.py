from langchain.llms import OpenAI 
from langchain.chat_models import ChatOpenAI

class ChatModel:
    def __init__(self, openai_api_key):
        self.llm_openai = OpenAI(model_name = "text-davinci-003", openai_api_key=openai_api_key)
        self.chat_model = ChatOpenAI(openai_api_key=openai_api_key)

    def predict(self, prompt):
        response = self.chat_model([prompt])
        return response