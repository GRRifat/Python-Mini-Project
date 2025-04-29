from tkinter import *
import datetime
from playsound import playsound
import threading

alarms = []

def update_current_time():
    now = datetime.datetime.now().strftime("%H:%M:%S")
    current_time_label.config(text=now)
    root.after(1000, update_current_time)

def set_alarm():
    set_time = f"{hour.get()}:{minute.get()}:{second.get()}"
    if set_time not in alarms:
        alarms.append(set_time)
        status_label.config(text=f"✅ Alarm set for {set_time}", fg="#4CAF50")
    else:
        status_label.config(text="⚠️ Alarm already set!", fg="#FF5722")

    def alarm_check():
        triggered = set()
        while True:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            if current_time in alarms and current_time not in triggered:
                alarm_message(current_time)
                triggered.add(current_time)
            elif current_time not in alarms:
                triggered.clear()
    
    threading.Thread(target=alarm_check, daemon=True).start()

def alarm_message(alarm_time):
    status_label.config(text=f"⏰ Alarm Triggered at {alarm_time}", fg="#2196F3")
    playsound("E:\Mini Project\Alarm Clock\song.mp3")

# ----- GUI Setup -----
root = Tk()
root.title("⏰ Stylish Alarm Clock")
root.geometry("450x350")
root.configure(bg="#F5F5F5")

# ----- Title -----
Label(root, text="🕒 Stylish Alarm Clock", font=("Helvetica", 22, "bold"), fg="#D32F2F", bg="#F5F5F5").pack(pady=15)

# ----- Time Display -----
Label(root, text="Current Time", font=("Helvetica", 14, "bold"), bg="#F5F5F5").pack()
current_time_label = Label(root, text="", font=("Helvetica", 18), fg="#333", bg="#F5F5F5")
current_time_label.pack()
update_current_time()

# ----- Time Set Frame -----
frame = Frame(root, bg="#F5F5F5")
frame.pack(pady=20)

def create_time_picker(label_text, variable, values, col):
    Label(frame, text=label_text, bg="#F5F5F5", font=("Helvetica", 12)).grid(row=0, column=col, padx=10)
    OptionMenu(frame, variable, *values).grid(row=1, column=col, padx=10)

hour = StringVar(root)
hour.set("00")
create_time_picker("Hour", hour, [str(i).zfill(2) for i in range(24)], 0)

minute = StringVar(root)
minute.set("00")
create_time_picker("Minute", minute, [str(i).zfill(2) for i in range(60)], 1)

second = StringVar(root)
second.set("00")
create_time_picker("Second", second, [str(i).zfill(2) for i in range(60)], 2)

# ----- Set Alarm Button -----
Button(root, text="Set Alarm", font=("Helvetica", 14), bg="#1976D2", fg="white", padx=20, pady=5, command=set_alarm).pack(pady=15)

# ----- Status Label -----
status_label = Label(root, text="", font=("Helvetica", 12), bg="#F5F5F5", fg="green")
status_label.pack()

root.mainloop()