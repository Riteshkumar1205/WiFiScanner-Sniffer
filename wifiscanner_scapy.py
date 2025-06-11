from scapy.all import *
from threading import Thread
import pandas as pd
import time
import os

# Initialize access point table
access_points = pd.DataFrame(columns=["SSID", "Signal(dBm)", "Channel", "Security"])
access_points.set_index("BSSID", inplace=True)

# Interface name (must be in monitor mode)
interface = "wlan0mon"

def data_extraction(packet):
    """Extract info from beacon frames"""
    if packet.haslayer(Dot11Beacon):
        bssid = packet[Dot11].addr2
        try:
            ssid = packet[Dot11Elt].info.decode('utf-8', errors='ignore')
        except:
            ssid = "<Hidden>"

        try:
            signal = packet.dBm_AntSignal
        except:
            signal = "N/A"

        stats = packet[Dot11Beacon].network_stats()
        channel = stats.get("channel")
        security = ", ".join(stats.get("crypto"))

        # Update data
        access_points.loc[bssid] = (ssid, signal, channel, security)

def print_all():
    """Continuously print updated WiFi info"""
    while True:
        os.system("clear")
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
        with pd.option_context('display.max_rows', 20, 'display.max_columns', None):
            print(access_points.sort_values(by="Signal(dBm)", ascending=False))
        print("\n[CTRL+C to stop scanning]")
        time.sleep(1)

def channel_hopper():
    """Cycle through channels 1-14"""
    ch = 1
    while True:
        os.system(f"iwconfig {interface} channel {ch}")
        ch = 1 if ch >= 14 else ch + 1
        time.sleep(0.5)

if __name__ == "__main__":
    print("[*] Starting WiFi scanner on interface:", interface)
    
    # Start threads
    Thread(target=print_all, daemon=True).start()
    Thread(target=channel_hopper, daemon=True).start()

    # Start packet sniffing
    sniff(prn=data_extraction, iface=interface, store=0)
