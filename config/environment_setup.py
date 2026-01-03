from dotenv import load_dotenv
import os
load_dotenv()

os.environ['GROQ_API_KEY']=os.getenv('GROQ_API_KEY')
os.environ['MODEL_NAME']=os.getenv('MODEL_NAME')
os.environ['EMBEDDING_MODEL_API_KEY']=os.getenv('EMBEDDING_MODEL_API_KEY')
os.environ['EMBEDDING_MODEL']=os.getenv('EMBEDDING_MODEL')
os.environ['LANGSMITH_TRACING']=os.getenv('LANGSMITH_TRACING')
os.environ['LANGSMITH_ENDPOINT']=os.getenv('LANGSMITH_ENDPOINT')
os.environ['LANGSMITH_API_KEY']=os.getenv('LANGSMITH_API_KEY')
os.environ['LANGSMITH_PROJECT']=os.getenv('LANGSMITH_PROJECT')