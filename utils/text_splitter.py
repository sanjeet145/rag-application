from langchain_text_splitters import RecursiveCharacterTextSplitter

class TextSplitter:
    def __init__(self,chunk_size=800, chunk_overlap=100):
        self.chunk_size=chunk_size
        self.chunk_overlap=chunk_overlap
        self._splitter = RecursiveCharacterTextSplitter(
            separators=['\n\n','\n'],
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap
        )
    def splitter(self,doc):
        return self._splitter.split_documents(doc)