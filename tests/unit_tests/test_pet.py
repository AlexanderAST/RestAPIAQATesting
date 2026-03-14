from config.base_test import BaseTest

class TestPet(BaseTest):
    

    def test_create_pet(self):
        pet = self.api_pet.create_pet()
        
        print(pet.id)