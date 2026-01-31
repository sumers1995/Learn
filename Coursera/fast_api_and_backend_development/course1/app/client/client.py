import requests

BASE_URL = "http://127.0.0.1:8000"

def get_users():
    response = requests.get(f"{BASE_URL}/shipment/", params={"id": 1185})
    print(response.json())

get_users()