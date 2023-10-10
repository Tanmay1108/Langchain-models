from ConcreteUnstructuredFileLoader import ConcreteUnstructuredFileLoader
from PythonLoaders.ConcretePythonLoader import ConcretePythonLoader
from PDFLoaders.ConcretePDFPlumberFileLoader import ConcretePDFPlumberFileLoader
from PDFLoaders.ConcretePDFMinerFileLoader import ConcretePDFMinerFileLoader
from PDFLoaders.ConcretePyMuPDFFileLoader import ConcretePyMuPDFFileLoader
from PDFLoaders.ConcretePyPDFFileLoader import ConcretePyPDFFileLoader
from PDFLoaders.ConcretePyPDFIum2FileLoader import ConcretePyPDFium2FileLoader
from HTMLLoaders.ConcreteUnstructuredHTMLFileLoader import ConcreteUnstructuredHTMLFileLoader
from HTMLLoaders.ConcreteBSHTMLFileLoader import ConcreteBSHTMLFileLoader
from PDFLoaders.ConcreteMathPixFileLoader import ConcreteMathpixPDFFileLoader
from JSONLoaders.ConcreteJSONFileLoader import ConcreteJSONFileLoader

def file_loader_factory(file_type='py', file_path=''):
    doc_loaders = {
        'py': ConcretePythonLoader,
        'py1': ConcreteUnstructuredFileLoader,
        'pdfminer': ConcretePDFMinerFileLoader,
        'pdfplumber': ConcretePDFPlumberFileLoader,
        'pdfpymu':ConcretePyMuPDFFileLoader,
        'pypdf': ConcretePyPDFFileLoader,
        'pypdfium':ConcretePyPDFium2FileLoader,
        'matpixpdf':ConcreteMathpixPDFFileLoader,
        'html': ConcreteUnstructuredHTMLFileLoader,
        'bs4html': ConcreteBSHTMLFileLoader,
        'pdf': ConcreteUnstructuredFileLoader,
        'json': ConcreteJSONFileLoader
    }
    return doc_loaders[file_type](file_path)
