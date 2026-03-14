import requests

from faker import Faker

HOST = "https://petstore3.swagger.io/api/v3"
PETID = 11


responce = requests.get(
    url="{}/pet/{}"
    .format(HOST, PETID)
)

fake = Faker()
print(fake.building_number())