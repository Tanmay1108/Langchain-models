from typing import Annotated
from Serializer.pdf_serializer import PDFSerializer
from fastapi import UploadFile
from fastapi import APIRouter, HTTPException
from Exceptions.exceptions import ValidationException

pdf_controller = APIRouter()

pdf_converters = {
    'pdfminer', 'pdfplumber', 'pdfpymu', 'pypdf', 'pypdfium'
}

@pdf_controller.post("/uploadfile/")
async def create_upload_file(file: UploadFile, pdfConverter: str):
    if pdfConverter not in pdf_converters:
        raise HTTPException(status_code=400, detail="PDF Converters can only be one of: {}".format(pdf_converters))
    pdf_serializer = PDFSerializer(file, pdfConverter)
    try:
        file_data = pdf_serializer.serialize()
    except Exception as e:
        if isinstance(e, ValidationException):
            raise HTTPException(status_code=400, detail=e.__str__)
        else:
            raise e #handle the 500 case. 
    return {"filename": file.filename, 'fileData': file_data}
