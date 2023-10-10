from DocLoaderSimpleFactory import file_loader_factory

if __name__ == "__main__":
    pdf_loader = file_loader_factory(file_type='bs4html', file_path='index.html')
    py_str = pdf_loader.return_text(page_length=1000)
    print(py_str)
