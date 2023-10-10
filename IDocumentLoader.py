from abc import ABC, abstractmethod

class IDocumentLoader(ABC):
    def __init__(self, file):
        self.file = file
    
    @abstractmethod
    def return_text(page_length:int):
        pass