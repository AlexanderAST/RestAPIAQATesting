

BASE_HOST = "https://petstore3.swagger.io/api/v3"

PET_BASE = f"{BASE_HOST}/pet"


class Endpoints:
    
    create_pet = PET_BASE
    update_pet = PET_BASE
    get_pet_by_status = f"{PET_BASE}/findByStatus"
    get_pet_by_tags = f"{PET_BASE}/findByTags"
    get_pet_by_id = lambda self, petId : f"{PET_BASE}/{petId}"
    update_pet_by_id = lambda self, petId: f"{PET_BASE}/{petId}"
    delete_pet_by_id = lambda self, petId: f"{PET_BASE}/{petId}"
    upload_pet_image_by_id = lambda self, petID: f"{PET_BASE}/{petID}"
    