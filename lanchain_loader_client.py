from DocLoaderSimpleFactory import file_loader_factory

if __name__ == "__main__":
    py_loader = file_loader_factory(file_type='py', file_path='test_file_1.py')
    py_str = py_loader.return_text(page_length=1000)
    print(py_str)