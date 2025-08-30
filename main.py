from fastapi import FastAPI
from pydantic import BaseModel
# backend/app/main.py
from .utils import check_drug_interactions, get_dosage_and_alternatives


app = FastAPI()

# Request models
class PrescriptionRequest(BaseModel):
    text: str

class DosageRequest(BaseModel):
    text: str
    age: int


# ✅ Endpoint: Drug Interaction Checker
@app.post("/check_interactions")
def check_interactions(request: PrescriptionRequest):
    medicines = request.text.split(",")  # naive extraction for now
    interactions = check_drug_interactions(medicines)
    return {"medicines": medicines, "interactions": interactions}


# ✅ Endpoint: Dosage & Alternatives
@app.post("/check_dosage_alternatives")
def check_dosage_alternatives(request: DosageRequest):
    medicines = request.text.split(",")
    dosage_info = get_dosage_and_alternatives(medicines, request.age)
    return {"medicines": medicines, "dosage_info": dosage_info}
