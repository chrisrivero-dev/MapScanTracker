# MapScanTracker

**A Tkinter-based desktop application for GIS and CAD technicians to log parcel cuts, scans, and map updates with automatic timestamps and Excel export support.**

Designed for transparency, efficiency, and easy adoption within **Assessor’s Office workflows**, MapScanTracker provides a modern way to track mapping progress while maintaining clean digital records.  
Built with **Python, Tkinter, pandas, and openpyxl**, it’s lightweight, portable, and easy to maintain.

![App Screenshot](assets/ScanMapsApp_UI.png)

---

## Features

- Simple Tkinter interface for fast data entry  
- Auto-logs date and timestamp with every record  
- Dropdowns for technician and software selection (ArcGIS Pro / MicroStation)  
- Saves entries to an Excel file (`Scan_Logs.xlsx`) in append mode  
- Clean, readable Python code built for portability and transparency  

---

## Tech Stack

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
git clone https://github.com/chrisrivero-dev/MapScanTracker.git
cd MapScanTracker


2️⃣ Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate   # On Windows use: venv\Scripts\activate

4️⃣ Launch the app
python ScanMapsApp.py

▶️ Usage

Run the app from your terminal:

python MapScanTracker.py


---

### ✅ After you do this:
Your “Installation” section will look perfect — with:
- Each command group in its own blue box  
- Bold headers outside the boxes  
- Proper separation between “Installation,” “Usage,” and “Author”  

---



