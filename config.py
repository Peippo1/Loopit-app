import os
from dotenv import load_dotenv

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
