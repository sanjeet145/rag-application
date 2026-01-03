from Ingestion.loadfile import loadpdf, loadtext
from utils.get_filetype import detect_file_type
from config.vector_db import vectorestore
from utils.text_splitter import TextSplitter
from utils.logger import logging

class Ingest:
    def __init__(self,doc,user_id):
        self._doc=doc
        self.user_id = user_id
    
    def ingest(self)->bool:
        try:
            file_type = detect_file_type(self._doc)
            if  file_type is None or file_type not in ['pdf','txt']:
                logging.error('Ingestion failed invalid file format')
                return False
            if detect_file_type(self._doc)=='pdf':
                self.docs = loadpdf(self._doc)
            if detect_file_type(self._doc)=='txt':
                self.docs = loadtext(self._doc)
            chunks = TextSplitter().splitter(self.docs)
            for chunk in chunks:
                chunk.metadata['user_id'] =self.user_id
            vectorestore.add_documents(chunks)
            logging.info('ingestion completed....')
            return True
        except Exception as e:
            logging.exception('Ingestion failed....\n'+str(e))
            return False