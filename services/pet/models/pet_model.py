from pydantic import BaseModel, field_validator


class PetModel(BaseModel):
    id: int
    name: str
    category: dict
    photoUrls: list
    tags: list
    status: str
    


response = {
    "id": 10,
    "name": "doggie",
    "category": {
        "id": 1,
        "name": "Dogs"
    },
    "photoUrls": [
        "string"
    ],
    "tags": [
        {
        "id": 0,
        "name": "string"
        }
    ],
    "status": "available"
}


user = PetModel(**response)

print(user.name)
print(user.category)
print(user.photoUrls)
print(user.tags)
print(user.status)