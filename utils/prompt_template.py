from langchain import PromptTemplate
from langchain.prompts import SystemMessagePromptTemplate, HumanMessagePromptTemplate, ChatPromptTemplate

# Define the prompt template for the system and human
def get_prompt_templates():
    prompt_temp_sistema = PromptTemplate(
        template="You are a virtual assistant recommending a/an {adjective} alternative to a product.",
        input_variables=["adjective"],
    )
    template_sistema = SystemMessagePromptTemplate(prompt=prompt_temp_sistema)

    prompt_temp_humano = PromptTemplate(template="{text}", input_variables=["text"])
    template_humano = HumanMessagePromptTemplate(prompt=prompt_temp_humano)

    chat_prompt = ChatPromptTemplate.from_messages([template_sistema, template_humano])
    
    return chat_prompt