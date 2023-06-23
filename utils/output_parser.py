from langchain.output_parsers import CommaSeparatedListOutputParser
from langchain.prompts import PromptTemplate

class IngredientListParser:
    def __init__(self):
        self.output_parser = CommaSeparatedListOutputParser()
        self.format_instructions = self.output_parser.get_format_instructions()

    def get_prompt_template(self, dish_name):
        basic_template_parser = f"""What are the ingredients to prepare {dish_name}\n{self.format_instructions}"""
        prompt_template = PromptTemplate(input_variables=["dish_name"], 
                                            template=basic_template_parser, 
                                            partial_variables={"how_to_parse": self.format_instructions})
        return prompt_template

    def parse_output(self, output):
        return self.output_parser.parse(output)