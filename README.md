## 📡 Real-Time WiFiScanner-Sniffer (Windows & Linux)

**WiFiScanner-Sniffer** is a Python-based wireless network monitoring tool that passively discovers nearby WiFi networks in real-time.

This lightweight, cross-platform application displays live SSID details, signal strength, operating channels, and encryption protocols — all from the comfort of a GUI (on Windows) or terminal (on Linux).  
It’s an educational and practical tool for WiFi troubleshooting, ethical reconnaissance, and signal analysis.

## ✅ Works on Windows & Linux (Kali, Ubuntu, Debian)

✅ Cross-platform: Windows (GUI) & Linux (monitor mode via `scapy`)  
📶 Real-time SSID, BSSID, signal strength, and channel mapping  
🖥️ Windows GUI using `tkinter`, `netsh`, and `pandas` (no root needed)  
🐧 Passive sniffing on Linux using `scapy` (requires monitor mode)  
🔒 Strictly passive – no packet injection, no unauthorized probing  
👩‍💻 Ideal for students, ethical hackers, wireless researchers, and trainers

---

## 🖥️ How to Use on Different OS

### 🪟 Windows (No Monitor Mode Required)

1. Open **Command Prompt** or **PowerShell**.
2. Run:
   ~~~bash
   git clone https://github.com/Riteshkumar1205/WiFiScanner-Sniffer.git
   cd WiFiScanner-Sniffer
   
   python -m venv venv
   venv\Scripts\activate
   
   pip install pandas nltk
   python python wifiscanner_scapy.py
   ~~~
3. A GUI will launch showing all visible WiFi networks with live signal updates.

---

### 🐧 Linux (Kali/Ubuntu/Debian — Requires Monitor Mode)

1. Open a Terminal.
2. Run:
   ~~~bash
   sudo apt update && sudo apt install git python3-pip aircrack-ng -y
   git clone https://github.com/Riteshkumar1205/WiFiScanner-Sniffer.git
   cd WiFiScanner-Sniffer
   
   pip3 install scapy pandas
   
   sudo airmon-ng start wlan0   # Replace wlan0 with your interface
   ~~~
   ## Run
   ~~~ 
   python3 wifiscanner_scapy.py
   ~~~
4. The terminal will display beacon frame data from surrounding WiFi networks.

---

## 📋 Features Overview

  | Feature              |     Windows GUI    |      Linux CLI   |
  |----------------------|--------------------|------------------|
  | SSID/BSSID Display   | ✅                 | ✅              |
  | Channel Mapping      | ✅                 | ✅              |
  | Signal Strength      | ✅                 | ✅              |
  | Encryption Detection | ✅                 | ✅              |
  | Monitor Mode Needed  | ❌                 | ✅              |
  | Internet Required    | ❌ (after install) | ❌ (after install) |

---

## 📄 License and Responsible Use

### 🔖 License

**This project is released under the MIT License**, a permissive open-source license that allows:

✔️ Personal, academic, or commercial use  
✔️ Modification and redistribution of the source code  
✔️ Integration into larger applications or teaching modules  


## 🧭 Ethical and Legal Use Policy

WiFiScanner-Sniffer is strictly intended for ethical, educational, and authorized wireless analysis.  
By using this tool, you agree to the following terms:

- ❌ You will **not** use this tool to scan networks you do not own or explicitly control.
- ✅ You will **only** use this on devices or environments where you have permission.
- ⚖️ You agree to comply with all **applicable cybersecurity, privacy, and data laws** in your region.
- ❗ The developer assumes **no responsibility** for any misuse, abuse, or illegal deployment of this software.

> ⚠️ This is a **passive educational tool**. It does **not** crack, inject, or interfere with wireless signals.

---


## 🧪 Final Note

**WiFiScanner-Sniffer is a learning-oriented, ethical tool — built with care to help others understand wireless environments safely. Use it wisely, share it responsibly, and never stop exploring the wireless world around you.**

