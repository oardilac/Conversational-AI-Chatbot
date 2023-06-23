from langchain.memory import ConversationBufferMemory

class ChatMemory:
    def __init__(self):
        self.memory = ConversationBufferMemory()
    
    def add_message(self, message):
        self.memory.add_message(message)
    
    def get_conversation(self):
        return self.memory.get_conversation()