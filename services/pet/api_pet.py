import requests
import allure

from services.pet.payloads import PayLoads
from services.pet.endpoints import Endpoints
from config.headers import Headers
from utils.helper import Helper
from services.pet.models.pet_model import PetModel

class PetAPI(Helper):
    def __init__(self):
        super().__init__()
        self.payloads = PayLoads()
        self.endpoints = Endpoints()
        self.headers = Headers()
    
    @allure.step("Create pet")    
    def create_pet(self):
        
        response = requests.post(
            url= self.endpoints.create_pet,
            json=self.payloads.create_update_pet
        )
        
        assert response.status_code == 200, response.json()
        
        self.attach_resonce(response.json())
        
        model = PetModel(**response.json())
        
        return model
        