import os
from dotenv import load_dotenv

load_dotenv()


class Headers:
    
    special_headers = {
        "api_key": f"{os.getenv('APIKEY')}"
    }