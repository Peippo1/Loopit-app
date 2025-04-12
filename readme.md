# LoopIt

LoopIt is a simple and visual habit tracker app built with Python. It helps you stay consistent by logging your daily habits and visualizing your progress using the Pixela API.

## 🚀 Features

- Track daily habit data (e.g., running, reading, etc.)
- Visualize progress via Pixela graphs
- Securely store credentials via `.env` file
- Modular, clean structure
- Ready for future GUI, notifications, and automation

## 🛠 Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Peippo1/Loopit-app.git
   cd Loopit-app
   ```

2. Create a virtual environment and activate it:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory and add your Pixela credentials:

   ```env
   PIXELA_USERNAME=your_username
   PIXELA_TOKEN=your_token
   PIXELA_GRAPH_ID=your_graph_id
   ```

## 🚴 Usage

Run the app with:

```bash
python main.py
```

You'll be prompted to enter your habit data (e.g. kilometers run) for the current day.

## 📦 Roadmap

- [ ] Add GUI with Tkinter or Streamlit
- [ ] Visual dashboard with charts
- [ ] Google Sheets export support
- [ ] Automated reminders & notifications
- [ ] Dockerize for deployment
- [ ] Deploy web version

## 🧠 License

MIT License. Feel free to use and improve!

---
Made with 💪 and Python.
