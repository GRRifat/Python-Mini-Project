import speedtest
from tkinter import *
from tkinter.ttk import Progressbar, Style
import threading
import os
from PIL import Image, ImageTk

# Create main window
root = Tk()
root.title("Internet Speed Tester - GR RIFAT")
root.geometry('420x420')
root.resizable(False, False)
root.configure(bg="#283593")  # Dark blue background

# Set window icon if available
if os.path.exists('speed.ico'):
    root.iconbitmap('speed.ico')

# Optional Logo
if os.path.exists('logo.png'):
    img = Image.open('logo.png').resize((60, 60))
    photo = ImageTk.PhotoImage(img)
    Label(root, image=photo, bg='#283593').pack(pady=(10, 0))

# Stylish title
Label(root, text="⚡ Internet Speed Test", bg="#283593", fg="#ffffff", font="Helvetica 24 bold").pack(pady=(5, 0))
Label(root, text="by GR RIFAT", bg="#283593", fg="#ffffff", font="Helvetica 13 italic").pack(pady=(0, 10))

# Result Frame (like a card)
frame = Frame(root, bg='white', bd=2, relief=RIDGE)
frame.place(x=40, y=120, width=340, height=170)

# Result Labels with unique colors for download, upload, ping, and server
down_label = Label(frame, text="⏬ Download Speed - ", bg='white', font='Arial 10 bold', fg="#388e3c")  # Green color for download
down_label.place(x=20, y=20)

up_label = Label(frame, text="⏫ Upload Speed - ", bg='white', font='Arial 10 bold', fg="#039be5")  # Light blue color for upload
up_label.place(x=20, y=50)

ping_label = Label(frame, text="Your Ping - ", bg='white', font='Arial 10 bold', fg="#fbc02d")  # Yellow color for ping
ping_label.place(x=20, y=80)

server_label = Label(frame, text="Server - ", bg='white', font='Arial 10 bold', fg="#8e24aa")  # Purple color for server
server_label.place(x=20, y=110)

# Variables for results
download_speed = upload_speed = ping_speed = 0
server_name = server_country = "Unknown"

# Speed test logic
def check_speed():
    global download_speed, upload_speed, ping_speed, server_name, server_country
    try:
        st = speedtest.Speedtest()
        st.get_best_server()

        download_speed = round(st.download() / 1_000_000, 2)
        upload_speed = round(st.upload() / 1_000_000, 2)
        ping_speed = round(st.results.ping, 2)

        server_name = st.results.server.get('sponsor', 'Unknown')
        server_country = st.results.server.get('country', 'Unknown')
    except Exception as e:
        download_speed = upload_speed = ping_speed = 0
        server_name = "Error"
        server_country = "Check Network"
        print("Speedtest error:", e)

def update_ui():
    thread = threading.Thread(target=check_speed)
    thread.start()

    progress = Progressbar(root, orient=HORIZONTAL, length=300, mode='indeterminate', style='Custom.Horizontal.TProgressbar')
    progress.place(x=60, y=300)
    progress.start()

    while thread.is_alive():
        root.update()

    # Update result labels with new colors
    down_label.config(text=f"⏬ Download Speed - {download_speed} Mbps")
    up_label.config(text=f"⏫ Upload Speed - {upload_speed} Mbps")
    ping_label.config(text=f"Your Ping - {ping_speed} ms")
    server_label.config(text=f"Server - {server_name}, {server_country}")

    progress.stop()
    progress.destroy()

# Custom style for progress bar
style = Style()
style.theme_use('default')
style.configure("Custom.Horizontal.TProgressbar", troughcolor='#ccc', background='#0288d1', thickness=10)

# Fancy Gradient Button
test_btn = Button(root, text="🚀 Start Test", font="Arial 11 bold", bg="#f44336", fg="white", width=30,
                  bd=0, activebackground="#d32f2f", padx=10, pady=8, command=update_ui)
test_btn.place(x=60, y=340)

root.mainloop()
