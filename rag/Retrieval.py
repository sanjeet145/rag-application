from config.vector_db import vectorestore
from langchain_core.documents import Document
from typing import List

def retrieve(query:str,user_id, k=4)->List[Document]:
    return vectorestore.similarity_search(
        query=query,
        k=k,
        filter={"user_id": user_id})