import tkinter as tk
from tkinter import messagebox
from api import add_pixel
from datetime import datetime
from reminder import start_reminder

def submit_data():
    try:
        quantity = float(entry.get())
        response = add_pixel(quantity)
        messagebox.showinfo("Pixela Response", response.text)
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number (e.g., 3.5)")

app = tk.Tk()
start_reminder()
app.title("LoopIt Tracker")

tk.Label(app, text="LoopIt - Habit Tracker", font=("Helvetica", 16)).pack(pady=10)

today_str = datetime.now().strftime("%d/%m/%Y")
tk.Label(app, text=f"Date: {today_str}", font=("Helvetica", 12)).pack(pady=5)

entry = tk.Entry(app, width=30)
entry.pack(pady=5)
entry.insert(0, "Enter kilometers")

submit_btn = tk.Button(app, text="Submit", command=submit_data)
submit_btn.pack(pady=10)

app.mainloop()
