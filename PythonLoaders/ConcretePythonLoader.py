from langchain.document_loaders import PythonLoader
from IDocumentLoader import IDocumentLoader

class ConcretePythonLoader(IDocumentLoader):
    def __init__(self, file):
        super().__init__(file)
        self.loader = PythonLoader(file)
        
    def return_text(self, page_length):
        docs = self.loader.load()
        return docs[0].page_content[:page_length]