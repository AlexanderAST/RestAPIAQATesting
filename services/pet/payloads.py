from faker import Faker
import random

fake = Faker()

class PayLoads:
    
    create_update_pet = {
        "id": random.randint(1000, 99999),
        "name": fake.first_name(),
        "category": {
            "id": 1,
            "name": "Dogs"
        },
        "photoUrls": [
            fake.image_url()
        ],
        "tags": [
            {
            "id": random.randint(1, 100),
            "name": fake.word()
            }
        ],
        "status": "available"
    }