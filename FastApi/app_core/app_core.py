from fastapi import FastAPI
from Controllers.pdf_controller import pdf_controller

app = FastAPI()

app.include_router(pdf_controller)