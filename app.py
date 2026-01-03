import config.environment_setup
from Ingestion.injest import Ingest
from rag.Retrieval import retrieve
from rag.Generation import RAG
from config.llm import llm

import streamlit as st

import os

class App:
    def __init__(self,user_id):
        self.user_id = user_id
    def ingest(self,file):
        ingestion = Ingest(file,self.user_id)
        ingested = ingestion.ingest()
        if not ingested:
            return False
        return True
    # rag
    def generate(self,query):
        rag = RAG(llm)
        retrieved_data= retrieve(query,self.user_id)
        response =rag.generate(query,retrieved_data)
        return response

# if __name__=='main()':
st.write("welcome to the rag application")
user_id=st.text_input('Enter the user id')

uploaded_file = st.file_uploader("Upload a file", type=["txt", "pdf"])

if uploaded_file is not None:
    st.write("Filename:", uploaded_file.name)

    content = uploaded_file.read()
    st.write("Raw bytes length:", len(content))

if 'app' not in st.session_state:
    st.session_state.app =None

if st.button("Submit"):
    if user_id is None:
        st.write('Please enter the user_id')
    st.session_state.app= App(user_id)
    if uploaded_file:
        save_path = os.path.join("uploads/", uploaded_file.name)
        os.makedirs("uploads", exist_ok=True) 
        
        with open(save_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        if st.session_state.app.ingest(save_path):
            st.write('Ingestion completed')
        else:
            st.write('Ingestion failed')
        if os.path.exists(save_path):
            os.remove(save_path)

query = st.text_input('Enter your query')
if st.button('query'):
    res =st.session_state.app.generate(query)
    st.write(res)