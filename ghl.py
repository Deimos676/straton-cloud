
import requests
import os
from dotenv import load_dotenv

load_dotenv()

GHL_API_KEY = os.getenv("GHL_API_KEY")
BASE_URL = "https://rest.gohighlevel.com/v1/contacts/"

headers = {
    "Authorization": f"Bearer {GHL_API_KEY}"
}

def get_leads():
    try:
        response = requests.get(BASE_URL, headers=headers)
        return response.json()
    except Exception as e:
        return {"error": str(e)}
