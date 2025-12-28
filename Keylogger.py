import tkinter as tk
import pynput
import json
from datetime import datetime

key_list = []

def log_key(event):
    key = event.char
    if key == "":
        key = event.keysym

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    key_data = {
        "time": timestamp,
        "key": key
    }
    key_list.append(key_data)

    
    with open("keystrokes.txt", "a") as f:
        f.write(f"{timestamp} : {key}\n")

    
    with open("keystrokes.json", "w") as jf:
        json.dump(key_list, jf, indent=4)

    output.insert(tk.END, key)
    output.see(tk.END)

root = tk.Tk()
root.title("Keylogger – Educational Demo")
root.geometry("500x300")

label = tk.Label(
    root,
    text="Type inside this box (Keystrokes will be logged)",
    font=("Arial", 12)
)
label.pack(pady=10)

output = tk.Text(root, height=8, width=55)
output.pack(pady=10)

note = tk.Label(
    root,
    text="Note: Captures keys only inside this window",
    fg="red"
)
note.pack()

root.bind("<Key>", log_key)

root.mainloop()
