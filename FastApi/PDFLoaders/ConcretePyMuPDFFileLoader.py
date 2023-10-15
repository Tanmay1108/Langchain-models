from langchain.document_loaders import PyMuPDFLoader
from PDFLoaders.IDocumentLoader import IDocumentLoader

class ConcretePyMuPDFFileLoader(IDocumentLoader):
    def __init__(self, file):
        super().__init__(file)
        self.loader = PyMuPDFLoader(file)
        
    def return_text(self, page_length):
        docs = self.loader.load()
        return docs[0].page_content[:page_length]
