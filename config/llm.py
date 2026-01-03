from langchain_groq import ChatGroq
import os

llm = ChatGroq(
    model=os.environ['MODEL_NAME'],
    reasoning_effort=None,
    verbose=False
    )

