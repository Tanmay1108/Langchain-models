from ConcreteUnstructuredFileLoader import ConcreteUnstructuredFileLoader

def file_loader_factory(file_type='py', file_path=''):
    doc_loaders = {
        'py': ConcreteUnstructuredFileLoader,
        'pdf': ConcreteUnstructuredFileLoader,
        'json': ConcreteUnstructuredFileLoader
    }
    return doc_loaders[file_type](file_path)