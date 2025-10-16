# 🗂️ ScanMapsApp

A **Tkinter-based desktop application** for GIS and CAD technicians to log parcel cuts, scans, and map updates with automatic timestamps and Excel export support.  
Designed for transparency, efficiency, and easy adoption within Assessor’s Office workflows.

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Tkinter](https://img.shields.io/badge/GUI-Tkinter-lightgrey.svg)](https://docs.python.org/3/library/tkinter.html)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![Built with Love](https://img.shields.io/badge/Built%20with❤️-Tkinter%20%26%20Pandas-orange.svg)](#)

---

## ✨ Features
- ✅ Simple Tkinter-based interface for fast data entry  
- 🕓 Auto-logs date and timestamp with every record  
- 🧭 Technician and software dropdowns (ArcGIS Pro / MicroStation)  
- 📊 Saves entries to an Excel file (`Scan_Logs.xlsx`) in append mode  
- ⚙️ Built for readability, portability, and transparency  

---

ScanMapsApp is a Python/Tkinter application developed by **Christopher Rivero** for the Orange County Assessor’s Office (Mapping Division).  
It simplifies how mapping technicians log and track completed map scans, providing an easy-to-use GUI for quick data entry and automatic Excel logging.

---

## ✨ Features

- 🧾 Simple Tkinter-based interface for fast data entry  
- 📅 Auto-logs date and timestamp with every record  
- 👩‍💻 Technician and software dropdowns (ArcGIS Pro / MicroStation)  
- 💾 Saves entries to an Excel file (`Scan_Logs.xlsx`) in append mode  
- 🧠 Built with readability, portability, and transparency in mind  


---
## 🚀 Usage Example

Run the app from your terminal:
```bash
python ScanMapsApp.py

## 🧠 Tech Stack

| Component | Description |
|------------|--------------|
| **Python 3.x** | Core application logic |
| **Tkinter** | GUI interface |
| **pandas / openpyxl** | Excel creation and export |
| **datetime / os** | Timestamp and file utilities |

---

## 📦 Installation

#### 1️⃣ Clone this repository
```bash
git clone https://github.com/chrisrivero-dev/ScanMapsApp.git
cd ScanMapsApp
python -m venv venv
source venv/bin/activate   # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
python ScanMapsApp.py

