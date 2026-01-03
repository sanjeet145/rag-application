from langchain_community.document_loaders import (
    PyMuPDFLoader,
    TextLoader
)


def loadpdf(file):
    return PyMuPDFLoader(file).load()

def loadtext(file):
    return TextLoader(file).load()