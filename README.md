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


Document for observations - https://docs.google.com/document/d/1EgWAq3ySzN97KytKMOexndFF__XWxErW0PwQ3LxxRpk/edit


Observations - 
PDF Observations - 
PDFPlumber

Analysis - 
Text is extracted out but the structure is not maintained. Tried for simple PDF’s there structure is maintained as well. 


Outputs - 
Functional Resume Sample
John W. Smith
2002 Front Range Way Fort Collins, CO 80525
jwsmith@colostate.edu
Career Summary
Four years experience in early childhood development with a diverse background in the care of
special needs children and adults.
Adult Care Experience
• Determined work placement for 150 special needs adult clients.
• Maintained client databases and records.
• Coordinated client contact with local health care professionals on a monthly basis.
• Managed 25 volunteer workers.
Childcare Experience
• Coordinated service assignments for 20 part-time counselors and 100 client families.
• Oversaw daily activity and outing planning for 100 clients.
• Assisted families of special needs clients with researching financial assistance and
healthcare.
• Assisted teachers with managing daily classroom activities.
• Oversaw daily and special student activities.
Employment History
1999-2002 Counseling Supervisor, The Wesley Center, Little Rock, Arkansas.
1997-1999 Client Specialist, R

PDFMiner - 
Analysis - 
Here better structure is maintained. The text is extracted correctly as well. 
Output - 
Functional Resume Sample 

John W. Smith  
2002 Front Range Way Fort Collins, CO 80525  
jwsmith@colostate.edu 

Career Summary 

Four years experience in early childhood development with a diverse background in the care of 
special needs children and adults.  

Adult Care Experience 

•  Determined work placement for 150 special needs adult clients.  
•  Maintained client databases and records.  
•  Coordinated client contact with local health care professionals on a monthly basis.     
•  Managed 25 volunteer workers.     

Childcare Experience 

•  Coordinated service assignments for 20 part-time counselors and 100 client families. 
•  Oversaw daily activity and outing planning for 100 clients.  
•  Assisted families of special needs clients with researching financial assistance and 

healthcare. 

•  Assisted teachers with managing daily classroom activities.    
•  Oversaw daily and special student activities.     

Employment History  

1999-2002 
1997-1999 
1996-1997 


PyMuPDF

Analysis - 
Similar to pdfminer, structure is maintained, but the tab spacing is lost.
Output - 
Functional Resume Sample 
 
John W. Smith  
2002 Front Range Way Fort Collins, CO 80525  
jwsmith@colostate.edu 
 
Career Summary 
 
Four years experience in early childhood development with a diverse background in the care of 
special needs children and adults.  
  
Adult Care Experience 
 
• Determined work placement for 150 special needs adult clients.  
• Maintained client databases and records.  
• Coordinated client contact with local health care professionals on a monthly basis.     
• Managed 25 volunteer workers.     
 
Childcare Experience 
 
• Coordinated service assignments for 20 part-time counselors and 100 client families. 
• Oversaw daily activity and outing planning for 100 clients.  
• Assisted families of special needs clients with researching financial assistance and 
healthcare. 
• Assisted teachers with managing daily classroom activities.    
• Oversaw daily and special student activities.     
 
Employment History  
 
1999-2002 
Counseling Supervisor, The Wesley

PyPDF
Analysis -
A better structure was maintained but text extracting had some faults. 
Output -
Functional Resume Sample 
 
John W. Smith   
2002 Front Range Way Fort Collins, CO 80525  
jwsmith@colostate.edu  
 
Career Summary 
 
Four years experience in early childhood development with a di verse background in the care of 
special needs children and adults.  
  
Adult Care Experience  
 
• Determined work placement for 150 special needs adult clients.  
• Maintained client databases and records.  
• Coordinated client contact with local health care professionals on a monthly basis.     
• Managed 25 volunteer workers.     
 
Childcare Experience  
 
• Coordinated service assignments for 20 part -time counselors and 100 client families. 
• Oversaw daily activity and outing planning for 100 clients.  
• Assisted families of special needs clients with researching financial assistance and 
healthcare. 
• Assisted teachers with managing daily classroom activities.    
• Oversaw daily and special st udent activities.     
 
Employment History  
 1999-2002  Counseling Supervisor, The 

PyPDFium


Analysis - 
A better structure and spacing was maintained, best till now, also had tab spaces.
Output - 
Functional Resume Sample 
John W. Smith 
2002 Front Range Way Fort Collins, CO 80525 
jwsmith@colostate.edu
Career Summary 
Four years experience in early childhood development with a diverse background in the care of 
special needs children and adults. 
Adult Care Experience
• Determined work placement for 150 special needs adult clients. 
• Maintained client databases and records. 
• Coordinated client contact with local health care professionals on a monthly basis. 
• Managed 25 volunteer workers. 
Childcare Experience
• Coordinated service assignments for 20 part-time counselors and 100 client families. 
• Oversaw daily activity and outing planning for 100 clients. 
• Assisted families of special needs clients with researching financial assistance and 
healthcare. 
• Assisted teachers with managing daily classroom activities. 
• Oversaw daily and special student activities. 
Employment History 
1999-2002 Counseling Supervisor, The Wesley Center, Little Rock, Ark

MatPixPDF
Did not have the api key so could not process the output. 

Unstructured


Analysis - 
Worst of all, it did not have any indentations or bullet new lines.. 

Output - 
Career Summary

Four years experience in early childhood development with a diverse background in the care of special needs children and adults.

Adult Care Experience

Determined work placement for 150 special needs adult clients. • Maintained client databases and records. • Coordinated client contact with local health care professionals on a monthly basis. • Managed 25 volunteer workers.

Childcare Experience

Coordinated service assignments for 20 part-time counselors and 100 client families. • Oversaw daily activity and outing planning for 100 clients. • Assisted families of special needs clients with researching financial assistance and healthcare.

Coordinated service assignments for 20 part-time counselors and 100 client families. • Oversaw daily activity and outing planning for 100 clients. • Assisted families of special needs clients with researching financial assistance and healthcare.

Assisted teachers with managing daily classroom activities. • Oversaw daily and special st


Python Observations - 


PyLoader - 
Analysis - 
Worked amazingly, had the perfect output.

Output -
import json
from tests.t_utils import compare_dict_response

url = "/corp/v1/corporate-users"
corp_user_group_url = "/corp/v1/corporate-user-groups"

def test_create_corp_user(client, data_provider, super_user_token):
    corp_user_data = data_provider.get_data("corp-user")[0]
    response = client.post(url, data=json.dumps(dict(data=corp_user_data)), content_type="application/json", headers=super_user_token)
    response_user = response.json.get("data")
    corp_user_data["isActive"] = True
    corp_user_data["version"] = 1
    assert response.status_code == 200
    assert response_user.get("corpUserId").startswith("CRUS")
    assert response_user.get("userName").get("firstName") == corp_user_data.get("userName").get("firstName")
    compare_dict_response(corp_user_data, response_user, exclude_list=["userName"])


def test_get_corp_user(client, data_provider, super_user_token):
    corp_user_data = data_provider.get_data("corp-user")[0]
    get_url = url + "?corpUserIds=CRUS1"
    res

Unstructured
Analysis - 
Faulty indentation, did not work appropriate.
Output - 
import json

from tests.t_utils import compare_dict_response

url = "/corp/v1/corporate



users"

corp_user_group_url = "/corp/v1/corporate



user



groups"

def test_create_corp_user(client, data_provider, super_user_token): corp_user_data = data_provider.get_data("corp-user")[0] response = client.post(url, data=json.dumps(dict(data=corp_user_data)), content_type="application/json", headers=super_user_token) response_user = response.json.get("data") corp_user_data["isActive"] = True corp_user_data["version"] = 1 assert response.status_code == 200 assert response_user.get("corpUserId").startswith("CRUS") assert response_user.get("userName").get("firstName") == corp_user_data.get("userName").get("firstName") compare_dict_response(corp_user_data, response_user, exclude_list=["userName"])

def test_get_corp_user(client, data_provider, super_user_token): corp_user_data = data_provider.get_data("corp-user")[0] get_url = url + "?corpUserIds=CRUS1" response = client.get(get_url, content_ty

JSON - 
UnstructuredHTML

Analysis - 
Works just fine for Json, the one which uses jq fails to iterate the same. 
Output - 
{
    "entity": "corp-user",
    "data": [
        {
            "userName": {"firstName": "Super", "middleName": "test", "lastName": "test lastname"},
            "phoneNumber": {"countryCode":"+91","number": "9999999990"},
            "organizationId": "Fake Org id",
            "corpEmail": "admin@delyvr.in"
        },
        {
            "groupName": "TestGroupName",
            "organizationId": "TestOrgId",
            "description": "test description"
        }
    ]
}

HTML - 
HTMLLoader

Analysis - 
Works fine. 
Output - 
texttttt

Sean made a change

BS4HTMLLoader - 

Analysis -
Incorporates the new lines and takes indentation into account. 

Output -



Spoon-Knife






  texttttt


  Sean made a change


