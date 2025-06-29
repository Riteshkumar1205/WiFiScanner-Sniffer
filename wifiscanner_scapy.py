import subprocess
import pandas as pd
import os
import time
import re
from threading import Thread

# DataFrame to store Access Point info
access_points = pd.DataFrame(columns=["SSID", "BSSID", "Signal (%)", "Channel", "Security"])

def parse_netsh_output():
    """Parse output from netsh wlan show networks mode=bssid"""
    try:
        output = subprocess.check_output("netsh wlan show networks mode=bssid", shell=True, encoding='utf-8', errors='ignore')
    except Exception as e:
        print(f"Error running netsh: {e}")
        return

    ssid, security = None, None
    ap_list = []

    for line in output.splitlines():
        line = line.strip()

        if line.startswith("SSID "):
            ssid_match = re.match(r"SSID \d+ : (.*)", line)
            ssid = ssid_match.group(1) if ssid_match else "<Hidden>"

        elif line.startswith("Authentication"):
            security = line.split(":", 1)[1].strip()

        elif line.startswith("BSSID"):
            bssid = line.split(":", 1)[1].strip()
        elif line.startswith("Signal"):
            signal = line.split(":", 1)[1].strip()
        elif line.startswith("Channel"):
            channel = line.split(":", 1)[1].strip()
            # Append only after collecting full AP block
            ap_list.append((ssid, bssid, signal, channel, security))

    # Update DataFrame
    global access_points
    access_points = pd.DataFrame(ap_list, columns=["SSID", "BSSID", "Signal (%)", "Channel", "Security"])
    access_points.set_index("BSSID", inplace=True)

def print_all():
    """Continuously print updated WiFi info"""
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print(r'''
╭────────────────────────────────────────────────────────────────────────────╮
│ ██╗    ██╗██╗███████╗██╗    ███████╗ ██████╗ █████╗ ███╗   ██╗███╗   ██╗     │
│ ██║    ██║██║██╔════╝██║    ██╔════╝██╔════╝██╔══██╗████╗  ██║████╗  ██║     │
│ ██║ █╗ ██║██║█████╗  ██║    ███████╗██║     ███████║██╔██╗ ██║██╔██╗ ██║     │
│ ██║███╗██║██║██╔══╝  ██║    ╚════██║██║     ██╔══██║██║╚██╗██║██║╚██╗██║     │
│ ╚███╔███╔╝██║██║     ██║    ███████║╚██████╗██║  ██║██║ ╚████║██║ ╚████║     │
│  ╚══╝╚══╝ ╚═╝╚═╝     ╚═╝    ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝     │
├────────────────────────── Author: ManuA | Version: 1.0 ─────────────────────┤
''')
        parse_netsh_output()
        with pd.option_context('display.max_rows', 20, 'display.max_columns', None):
            print(access_points.sort_values(by="Signal (%)", ascending=False))
        print("\n[CTRL+C to stop scanning]")
        time.sleep(3)

if __name__ == "__main__":
    print("[*] Scanning for WiFi networks using netsh (Windows)...")
    try:
        Thread(target=print_all, daemon=True).start()
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[!] Scan stopped by user.")
