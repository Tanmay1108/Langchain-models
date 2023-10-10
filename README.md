# Langchain-models
Creating and testing various langchain models for processing PDF, JSON and python files.

Steps for setup (for macbook) - 

pip install lanchain

pip install openai

Langchain documentation

Langchain git link

pip install "unstructured[local-inference]"

pip install cython

pip3 install torch torchvision torchaudio

git clone https://github.com/facebookresearch/detectron2.git

cd into detectron2 folder and do pip install -e .

Then go back to root dir, pip install opency-python

pip install "layoutparser[layoutmodels, tesseract]"

pip install python-magic

pip install python-magic-bin/pip install libmagic

Brew install tesseract

brew install poppler

pip install poppler-utils

Pip install pytesseract (for images in pdfs)

For document files (.doc and .docx) do install libreoffice

python -c "import nltk; nltk.download('punkt')"

Create a file with following code and run it - 
```
import nltk
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download(‘punkt’)
nltk.download(‘averaged_perceptron_tagger’)
```

pip install faiss-cpu

pip install tiktoken


UML for the design - 

![Langchain2](https://github.com/Tanmay1108/Langchain-models/assets/46091259/7bbbe978-1df4-470c-9cb1-8891d6a4fb33)



