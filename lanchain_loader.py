from langchain.document_loaders import UnstructuredFileLoader, PyPDFLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS

loader = UnstructuredFileLoader("test_file_1.py")
# loader = PyPDFLoader("test_file_1.py")

docs = loader.load()
text_splitter = CharacterTextSplitter(
    separator = "\n",
    chunk_size = 800,
    chunk_overlap = 200,
    length_function = len
)
texts = text_splitter.split_text(docs[0].page_content)

embeddings = OpenAIEmbeddings()

document_search = FAISS.from_texts(texts, embeddings)


print(docs[0].page_content[:1000])
