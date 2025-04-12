# LoopIt - A Habit Tracker App
import requests
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

USERNAME = os.getenv("PIXELA_USERNAME")
TOKEN = os.getenv("PIXELA_TOKEN")
GRAPH_ID = os.getenv("PIXELA_GRAPH_ID")

required_vars = {
    "PIXELA_USERNAME": USERNAME,
    "PIXELA_TOKEN": TOKEN,
    "PIXELA_GRAPH_ID": GRAPH_ID,
}

missing = [key for key, value in required_vars.items() if not value]
if missing:
    raise EnvironmentError(f"Missing required environment variables: {', '.join(missing)}")

from api import add_pixel

today = datetime.now()
print(today.strftime("%d/%m/%Y - LoopIt"))

quantity = input("How many kilometers did you run today? ")
response = add_pixel(quantity)
print(response.text)
