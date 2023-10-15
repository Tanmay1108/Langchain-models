from Factories.DocLoaderSimpleFactory import file_loader_factory
import shutil
from pathlib import Path
from tempfile import NamedTemporaryFile
from fastapi import UploadFile
from Exceptions.exceptions import ValidationException

class PDFSerializer():
    def __init__(self, file, pdf_controller):
        self.file = file
        self.pdf_controller = pdf_controller
        
    def _save_upload_file_tmp(self, upload_file: UploadFile) -> Path:
        try:
            suffix = Path(upload_file.filename).suffix
            with NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
                shutil.copyfileobj(upload_file.file, tmp)
                tmp_path = Path(tmp.name)
        finally:
            upload_file.file.close()
        return tmp_path

    def serialize(self):
        file_path = self._save_upload_file_tmp(self.file)
        pdf_loader = file_loader_factory(file_type=self.pdf_controller, file_path=str(file_path))
        try:
            py_str = pdf_loader.return_text(page_length=1000)
        except Exception as e:
            raise ValidationException(message="Can not parse the file: error {}".format(str(e)))
        return py_str