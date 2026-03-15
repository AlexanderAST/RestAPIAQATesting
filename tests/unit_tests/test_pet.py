import allure
import pytest

from config.base_test import BaseTest

@allure.epic("Administration")
@allure.feature("Pet")
class TestPet(BaseTest):
    
    @allure.title("Create new pet")
    def test_create_pet(self):
        pet = self.api_pet.create_pet()
        self.api_pet.get_pet_by_id(pet.id)