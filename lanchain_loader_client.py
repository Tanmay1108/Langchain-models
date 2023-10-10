# from langchain.document_loaders import UnstructuredFileLoader, PyPDFLoader
# from langchain.embeddings.openai import OpenAIEmbeddings
# from langchain.text_splitter import CharacterTextSplitter
# from langchain.vectorstores import FAISS
# from abc import ABC, abstractmethod

# # loader = UnstructuredFileLoader("test_file_1.py")
# # # loader = PyPDFLoader("test_file_1.py")

# # docs = loader.load()
# # text_splitter = CharacterTextSplitter(
# #     separator = "\n",
# #     chunk_size = 800,
# #     chunk_overlap = 200,
# #     length_function = len
# # )
# # texts = text_splitter.split_text(docs[0].page_content)

# # embeddings = OpenAIEmbeddings()

# # document_search = FAISS.from_texts(texts, embeddings)


# # print(docs[0].page_content[:1000])

# class IDocumentLoader(ABC):
#     def __init__(self, file):
#         self.file = file
    
#     @abstractmethod
#     def return_text(page_length:int):
#         pass

# class ConcreteUnstructuredFileLoader(IDocumentLoader):
#     def __init__(self, file):
#         super().__init__(file)
#         self.loader = UnstructuredFileLoader(file)
        
#     def return_text(self, page_length):
#         docs = self.loader.load()
#         return docs[0].page_content[:page_length]

# def file_loader_factory(file_type='py', file_path=''):
#     doc_loaders = {
#         'py': ConcreteUnstructuredFileLoader,
#         'pdf': ConcreteUnstructuredFileLoader,
#         'json': ConcreteUnstructuredFileLoader
#     }
#     return doc_loaders[file_type](file_path)

from DocLoaderSimpleFactory import file_loader_factory


if __name__ == "__main__":
    py_loader = file_loader_factory(file_type='py', file_path='test_file_1.py')
    py_str = py_loader.return_text(page_length=1000)
    print(py_str)