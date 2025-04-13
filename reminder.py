from pync import Notifier
import schedule
import time
import threading

def send_reminder():
    Notifier.notify("Don't forget to log your habit in LoopIt!", title="LoopIt Reminder")

def start_reminder():
    schedule.every().day.at("10:00").do(send_reminder)  # Update time as needed

    def loop():
        while True:
            schedule.run_pending()
            time.sleep(60)

    threading.Thread(target=loop, daemon=True).start()
