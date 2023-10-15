from PDFLoaders.ConcretePDFPlumberFileLoader import ConcretePDFPlumberFileLoader
from PDFLoaders.ConcretePDFMinerFileLoader import ConcretePDFMinerFileLoader
from PDFLoaders.ConcretePyMuPDFFileLoader import ConcretePyMuPDFFileLoader
from PDFLoaders.ConcretePyPDFFileLoader import ConcretePyPDFFileLoader
from PDFLoaders.ConcretePyPDFIum2FileLoader import ConcretePyPDFium2FileLoader


def file_loader_factory(file_type='py', file_path=''):
    doc_loaders = {
        'pdfminer': ConcretePDFMinerFileLoader,
        'pdfplumber': ConcretePDFPlumberFileLoader,
        'pdfpymu':ConcretePyMuPDFFileLoader,
        'pypdf': ConcretePyPDFFileLoader,
        'pypdfium':ConcretePyPDFium2FileLoader
    }
    return doc_loaders[file_type](file_path)
