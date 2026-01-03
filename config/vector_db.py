from langchain_chroma import Chroma
from .embedding import embedding

vectorestore = Chroma(
    embedding_function=embedding,
    persist_directory='./chromadb'
    )