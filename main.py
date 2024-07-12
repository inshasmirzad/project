 
from fastapi import FastAPI,HTTPException
#from data import patients_dict
from typing import Optional
from models import PatientBaseModel
from models import GenderEnum
app = FastAPI()

# @app.get("/")
# async def read_root():
#     return {"Hello": "World"}

@app.get("/name/{name_of_lab}")
async def get_name(names: str):
    return {"message":names}

# @app.get("/name/names/{age}")
# async def get_age(age : int):
#     return {"message": f"{age}"}

from data import patients_dict
@app.get("/patients")
async def get_details():
    return list(patients_dict.values())

@app.get("/patients/{patientname}")
async def get_details_of_each(patientname : str):
    if patientname not in patients_dict:
        raise HTTPException(status_code=404)

    return patients_dict[patientname]

@app.get("/patients/gender/{gender}")
async def get_by_gendre(gender: GenderEnum):
    all_patients=list(patients_dict.values())
    patient_gender=[]
    for patients in all_patients:
        if patients["gender"] == gender.value:
            patient_gender.append(patients)
    return patient_gender

@app.post("/patient/patients")
async def new_patient(patient:PatientBaseModel):
    patients_dict[patient.name]=patient.dict()
    return {"message":f"{patient.name} is successfully added"}

@app.get("/patients/search/")
async def search_patients_by_unique(medical_history:Optional[str]=None,prescriptions:Optional[str]=None,lab_results:Optional[str]=None):
    results = []
    for patient in patients_dict.values():
        if (medical_history and medical_history in patient["medical_history"]) or \
           (prescriptions and prescriptions in patient["prescriptions"]) or \
           (lab_results and lab_results in patient["lab_results"]):
            results.append(patient)
    return results

@app.put("/patients/{name}")
async def update_patient(name: str, patient: PatientBaseModel):
    if name not in patients_dict:
        raise HTTPException(status_code=404, detail="Patient not found")
    patients_dict[name] = patient.dict()
    return {"message": "Patient updated successfully"}

@app.delete("/patients/{name}")
async def delete_patient(name: str):
    if name not in patients_dict:
        raise HTTPException(status_code=404, detail="Patient not found")
    del patients_dict[name]
    return {"message": "Patient deleted successfully"}

@app.get("/patients/")
async def get_limit_patients(skip: int = 0, limit: int = 10):
    patients = list(patients_dict.values())
    return patients[skip: skip + limit]




    
