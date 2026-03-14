from services.pet.api_pet import PetAPI

def main():
    pet = PetAPI()
    
    pet.create_pet()


if __name__ == "__main__":
    main()