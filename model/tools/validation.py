import re

def person_id_validator(person_id):
    if re.match(r"^[a-zA-Z\d\s]{3,30}$",person_id):
        return True
    else:
        return False

def medical_validator(medical):
    if re.match(r"^[a-zA-Z\s]{3,30}$",medical):
        return True
    else:
        return False