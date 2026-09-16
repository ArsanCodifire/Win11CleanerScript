import ctypes
import os
import sys


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except Exception:
        return False


if not is_admin():
    params = " ".join(f'"{arg}"' for arg in sys.argv)

    ctypes.windll.shell32.ShellExecuteW(
        None,
        "runas",
        sys.executable,
        params,
        None,
        1
    )

    sys.exit()
    
#Main

import customtkinter as ctk
import threading
import cleaner

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Cleaner")
app.geometry("900x700")
app.resizable(False, False)

last_result = None

title = ctk.CTkLabel(
    app,
    text="🧹 Windows Cleaner",
    font=("Segoe UI", 30, "bold")
)
title.pack(pady=20)

frame = ctk.CTkFrame(app)
frame.pack(fill="both", expand=True, padx=20, pady=10)

status = ctk.CTkLabel(frame, text="Ready", font=("Segoe UI", 22, "bold"))
status.pack(pady=15)

deleted = ctk.CTkLabel(frame, text="Deleted Files : 0", font=("Segoe UI", 18))
deleted.pack(anchor="w", padx=30)

skipped = ctk.CTkLabel(frame, text="Skipped Files : 0", font=("Segoe UI", 18))
skipped.pack(anchor="w", padx=30)

space = ctk.CTkLabel(frame, text="Space Freed : 0 MB", font=("Segoe UI", 18))
space.pack(anchor="w", padx=30)

time_label = ctk.CTkLabel(frame, text="Time : 0.00 s", font=("Segoe UI", 18))
time_label.pack(anchor="w", padx=30)

ctk.CTkLabel(frame, text="Folders", font=("Segoe UI", 20, "bold")).pack(
    anchor="w", padx=30, pady=(20, 5)
)

folder_labels = {}

for name in [
    "Temp",
    "Windows Temp",
    "DirectX Shader Cache",
    "Windows Error Reports",
    "Thumbnail Cache",
]:
    lbl = ctk.CTkLabel(frame, text=f"{name} : 0")
    lbl.pack(anchor="w", padx=50)

    folder_labels[name] = lbl

def update_ui(data):
    global last_result

    last_result = data

    status.configure(text=data["status"])

    deleted.configure(text=f"Deleted Files : {data['deleted']}")
    skipped.configure(text=f"Skipped Files : {data['skipped']}")
    space.configure(text=f"Space Freed : {data['freed_mb']:.2f} MB")
    time_label.configure(text=f"Time : {data['time']} s")

    for name, lbl in folder_labels.items():
        lbl.configure(text=f"{name} : {data['folders'].get(name, 0)}")

    clean_btn.configure(state="normal")

def show_details(data):
    if data is None:
        return

    win = ctk.CTkToplevel(app)
    win.title("Cleanup Details")
    win.geometry("650x400")

    box = ctk.CTkTextbox(win)
    box.pack(fill="both", expand=True, padx=10, pady=10)

    box.insert("end", f"Status : {data['status']}\n")
    box.insert("end", f"Deleted : {data['deleted']}\n")
    box.insert("end", f"Skipped : {data['skipped']}\n")
    box.insert("end", f"Space Freed : {data['freed_mb']:.2f} MB\n")
    box.insert("end", f"Time : {data['time']} s\n\n")
    box.insert("end", "Folders Cleaned\n")
    box.insert("end", "=" * 50 + "\n")

    for name, count in data["folders"].items():
        box.insert("end", f"{name}: {count}\n")

    box.insert("end", "\n")

    box.insert("end", "Skipped Items\n")
    box.insert("end", "=" * 50 + "\n")

    if not data["skipped_items"]:
        box.insert("end", "None 🎉")
    else:
        for item in data["skipped_items"]:
            box.insert("end", f"• {item['name']}\n")
            box.insert("end", f"Path: {item['path']}\n")
            box.insert("end", f"Reason: {item['reason']}\n\n")

    box.configure(state="disabled")

def run_clean():
    data = cleaner.clean()
    app.after(0, lambda: update_ui(data))


def clean_now():
    status.configure(text="Cleaning...")
    clean_btn.configure(state="disabled")
    threading.Thread(target=run_clean, daemon=True).start()

clean_btn = ctk.CTkButton(
    app,
    text="🧹 Clean Now",
    command=clean_now,
    width=250,
    height=45
)
clean_btn.pack(pady=20)

details_btn = ctk.CTkButton(
    app,
    text="📋 Details",
    command=lambda: show_details(last_result),
    width=250,
    height=40
)
details_btn.pack(pady=20)

app.mainloop()
