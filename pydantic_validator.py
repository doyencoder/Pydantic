from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Optional, Dict, Annotated

class Patient(BaseModel):
    name: str = Annotated[str, Field(min_length=2, max_length=50, description="Full name of the patient")]
    email: EmailStr
    website: Optional[AnyUrl] = None
    age: int = Field(..., gt=0, lt=100, description="Age must be a positive integer")
    weight: Annotated[float, Field(gt=0.0, lt=500.0, description="Weight in kilograms", strict=True)]
    married: Annotated[bool, Field(default=False, description="Marital status of the patient")]
    allergies: Optional[List[str]] = Field(default=None, max_items=5)
    contact_details: Dict[str, str]

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("Data inserted successfully")

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("Data updated successfully")

patient_info =  {'name': 'rajat', 'email': 'rajat@example.com', 'website': 'http://example.com', 'age': 20, 'weight': 80.5, 'married': False, 'allergies': ['dust','tea'], 'contact_details': {'phone': '1234567890'}}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)