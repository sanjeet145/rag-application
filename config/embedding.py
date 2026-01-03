from langchain_huggingface import HuggingFaceEmbeddings
import os

embedding=HuggingFaceEmbeddings(model_name=os.environ['EMBEDDING_MODEL'])