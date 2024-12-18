from pydantic import BaseModel, EmailStr, field_validator

class Utilisateur(BaseModel):
    nom: str
    age: int
    email: EmailStr

    @field_validator('age')
    def check_age(value):
        if value < 18:
            raise ValueError('Il faut etre majeur !')
        return value

try:
    bill = Utilisateur(nom='Bill', age=17, email='bill@example.com')
except ValueError as e:
    print('Erreur :', e)
