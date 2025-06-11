## 📌 Description
**WiFiScanner-Visualizer is a lightweight, Python-based terminal tool designed to passively monitor and visualize nearby wireless networks. Built using the Scapy library, it listens for 802.11 beacon frames and extracts live information such as:**

📶 SSID (Network Name)

📡 Signal Strength (dBm)

📻 Operating Channel

## 🔐 Security Protocol (e.g., WPA2, WEP)

This tool helps users analyze the wireless environment, detect overlapping channels, and assess signal quality — which is especially useful for home network optimization, classroom demonstrations, and WiFi research.

## ⚠️ Important:
This tool does not perform any packet injection, cracking, or unauthorized access. It operates passively, capturing only broadcasted management frames (beacons). Use it only on networks you own or have explicit permission to monitor.

## ✅ Use Cases
Troubleshooting weak WiFi coverage

Classroom demonstrations on wireless signals

Detecting crowded or overlapping WiFi channels

Basic wireless reconnaissance (within legal/ethical boundaries)

Verifying router visibility and encryption types



## 💻 How to Use
**⚠️ Interface must be in monitor mode for the tool to function properly.**

## 🐧 Linux (Kali, Ubuntu)
**Enable monitor mode:**

bash
**sudo airmon-ng start wlan0**
Replace wlan0 with your adapter name (check with iwconfig or ip a).

Run the scanner:

bash

**python3 wifiscanner_scapy.py**
## 🍏 macOS

**Monitor mode support depends on your chipset and drivers. This tool is tested primarily on Linux.**

**📁 Clone the Repository**
bash

git clone https://github.com/RiteshKumar/WiFiScanner-Visualizer.git
cd WiFiScanner-Visualizer

## 📄 License & Ethical Use
**This project is licensed under the MIT License, which permits personal, academic, and commercial use with proper attribution.**

**🚨 Important Notice**
This tool is intended for ethical and educational use only.
You must not use it for:

Scanning networks you do not own or lack permission to analyze

Performing any kind of unauthorized surveillance

Violating any applicable laws or institutional policies

Always ensure that your activities comply with local cybersecurity laws, ethical standards, and privacy regulations.



