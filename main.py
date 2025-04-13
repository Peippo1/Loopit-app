# LoopIt - A Habit Tracker App
import requests
from datetime import datetime
from dotenv import load_dotenv
import os
from rich.console import Console
from rich.panel import Panel
from rich import box
from reminder import start_reminder

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

console = Console()
start_reminder()

today = datetime.now()
console.print(Panel(f"[bold green]{today.strftime('%d/%m/%Y')} - LoopIt[/bold green]", expand=False, box=box.ROUNDED))

while True:
    try:
        quantity = float(input("How many kilometers did you run today? "))
        break
    except ValueError:
        console.print("[bold red]Invalid input![/bold red] Please enter a valid number (e.g., 3.5)")

response = add_pixel(quantity)
console.print(Panel(f"[bold cyan]Pixela Response:[/bold cyan]\n{response.text}", expand=False))
