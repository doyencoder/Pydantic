from pydantic import BaseModel

class Address(BaseModel):

    city: str
    state: str
    pin: str

class Patient(BaseModel):

    name: str
    gender: str
    age: int
    address: Address

address_dict = {'city': 'mathura', 'state': 'U.P.', 'pin': '221001'}

address1 = Address(**address_dict)

patient_dict = {'name': 'rajat', 'gender': 'male', 'age': 20, 'address': address1}

patient1 = Patient(**patient_dict)

print(patient1)
