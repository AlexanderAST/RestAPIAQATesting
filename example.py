import requests

HOST = "https://petstore3.swagger.io/api/v3"
PETID = 11


responce = requests.get(
    url="{}/pet/{}"
    .format(HOST, PETID)
)

print(responce.json())