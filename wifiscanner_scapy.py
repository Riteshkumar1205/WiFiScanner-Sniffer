import subprocess
import pandas as pd
import re
import time
import tkinter as tk
from tkinter import ttk
import nltk
from nltk.corpus import stopwords
import threading

# Ensure nltk data is downloaded
nltk.download('stopwords', quiet=True)
stop_words = set(stopwords.words('english'))

# WiFi DataFrame
access_points = pd.DataFrame(columns=["SSID", "BSSID", "Signal", "Channel", "Security"])

def clean_ssid(ssid):
    """Filter out stopwords from SSID names."""
    words = ssid.split()
    filtered = [word for word in words if word.lower() not in stop_words]
    return ' '.join(filtered)

def scan_wifi():
    """Scan nearby WiFi networks using netsh."""
    try:
        output = subprocess.check_output("netsh wlan show networks mode=bssid", shell=True, encoding='utf-8', errors='ignore')
    except Exception as e:
        print(f"[ERROR] {e}")
        return

    ssid, security = None, None
    results = []

    for line in output.splitlines():
        line = line.strip()
        if line.startswith("SSID "):
            match = re.match(r"SSID \d+ : (.*)", line)
            ssid = match.group(1) if match else "<Hidden>"
            ssid = clean_ssid(ssid)
        elif line.startswith("Authentication"):
            security = line.split(":", 1)[1].strip()
        elif line.startswith("BSSID"):
            bssid = line.split(":", 1)[1].strip()
        elif line.startswith("Signal"):
            signal = line.split(":", 1)[1].strip()
        elif line.startswith("Channel"):
            channel = line.split(":", 1)[1].strip()
            results.append((ssid, bssid, signal, channel, security))

    global access_points
    access_points = pd.DataFrame(results, columns=["SSID", "BSSID", "Signal", "Channel", "Security"])
    access_points.set_index("BSSID", inplace=True)

def update_table():
    """Update the tkinter table every few seconds."""
    while True:
        scan_wifi()
        for item in tree.get_children():
            tree.delete(item)
        for idx, row in access_points.iterrows():
            tree.insert("", "end", values=(row["SSID"], idx, row["Signal"], row["Channel"], row["Security"]))
        time.sleep(5)

# GUI Setup
root = tk.Tk()
root.title("WiFi Network Scanner (Windows)")
root.geometry("1000x500")
root.resizable(False, False)

# ASCII Banner at the top
banner = r'''
╭────────────────────────────────────────────────────────────────────────────╮
│ ██╗    ██╗██╗███████╗██╗    ███████╗ ██████╗ █████╗ ███╗   ██╗███╗   ██╗     │
│ ██║    ██║██║██╔════╝██║    ██╔════╝██╔════╝██╔══██╗████╗  ██║████╗  ██║     │
│ ██║ █╗ ██║██║█████╗  ██║    ███████╗██║     ███████║██╔██╗ ██║██╔██╗ ██║     │
│ ██║███╗██║██║██╔══╝  ██║    ╚════██║██║     ██╔══██║██║╚██╗██║██║╚██╗██║     │
│ ╚███╔███╔╝██║██║     ██║    ███████║╚██████╗██║  ██║██║ ╚████║██║ ╚████║     │
│  ╚══╝╚══╝ ╚═╝╚═╝     ╚═╝    ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝     │
├────────────────────────── Author: ManuA | Version: 1.0 ─────────────────────┤
'''
label_banner = tk.Label(root, text=banner, font=("Courier", 9), justify="left", fg="green", bg="black")
label_banner.pack(padx=10, pady=5, fill=tk.X)

# Table for displaying APs
columns = ("SSID", "BSSID", "Signal", "Channel", "Security")
tree = ttk.Treeview(root, columns=columns, show="headings")

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=180 if col == "BSSID" else 120)

tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

# Launch background thread
threading.Thread(target=update_table, daemon=True).start()

# Start GUI loop
root.mainloop()
