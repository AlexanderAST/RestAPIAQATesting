from pydantic import BaseModel, field_validator


class PetModel(BaseModel):
    id: int
    name: str
    category: dict
    photoUrls: list
    tags: list
    status: str
    
    @field_validator("id", "name", "category", "tags", "status")
    def fields_are_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError("Field cannot be empty")
        else:
            return value
        

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