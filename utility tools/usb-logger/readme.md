# 🧩 USB Device Logger (Windows)

A simple Python utility that **logs all USB devices** that are connected or disconnected from your Windows computer — including flash drives, phones, keyboards, etc.

---

## 📦 Features

- 🟢 Detects **all** USB device connections and disconnections (not just storage)
- 📄 Logs each event to `usb_log.txt`
- 🧠 Uses **Windows WMI** to monitor system-level USB events
- 💡 Displays device IDs and timestamps in real-time

---

## 🛠️ Requirements

- Python 3.7+
- Windows OS
- Install WMI for Python:

```bash
pip install wmi
```
## 🚀 Usage
Save the script below as usb_logger.py:

Run it from your terminal or IDE:

```bash
python usb_logger.py
```
You’ll see output in the terminal and in usb_log.txt.


## ⚠️ Notes
- This script requires admin permissions to access full WMI USB events on some systems.

- It only runs on Windows.

## 🔧 To-Do / Enhancements
 - Show human-readable device names

 - Export to CSV or SQLite

 - Run as a background Windows service

 - Create a GUI version

## 📜 License
MIT — use it freely, modify as needed.

## ✨ Author
Built by Asa Herrin

Feel free to fork, improve, or report issues!