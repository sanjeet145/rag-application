from langchain_core.output_parsers import StrOutputParser
from utils.prompt import SYSTEM_PROMPT

class RAG:
    def __init__(self, llm):
        self.llm =llm
        self.output_parser = StrOutputParser()
        self.SYSTEM_PROMPT =SYSTEM_PROMPT
    
    def generate(self,query,retrieved_data):
        prompt_text=f'{self.SYSTEM_PROMPT}\n\n retrieved context: \n {retrieved_data}'
        messages = [
            {"role": "system", "content": prompt_text},
            {"role": "user", "content": query}
        ]
        chain = self.llm|self.output_parser
        res= chain.invoke(messages)
        return res.split('</think>')[1]
        