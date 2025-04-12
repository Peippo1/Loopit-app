import requests
import os
from datetime import datetime
from config import USERNAME, TOKEN, GRAPH_ID

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
HEADERS = {
    "X-USER-TOKEN": TOKEN
}

def add_pixel(quantity):
    pixel_creation_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"
    today = datetime.now().strftime("%Y%m%d")
    pixel_data = {
        "date": today,
        "quantity": str(quantity),
    }
    response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=HEADERS)
    return response
