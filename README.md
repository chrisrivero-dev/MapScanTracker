# ScanMapsApp

**Local Desktop Tool for Tracking and Logging Completed Assessor Map Scans**

ScanMapsApp is a lightweight Python/Tkinter application designed to simplify how the Orange County Assessor’s Office Mapping Division logs and tracks completed map scans.  
It provides a user-friendly interface for technicians to record cut numbers, software used (ArcGIS Pro or MicroStation), employee names, and timestamps — automatically exporting data to Excel for central tracking.

---

## Features

- Simple Tkinter-based GUI for easy data entry  
- Automatic timestamp logging for every record  
- Exports all entries to a shared Excel file (auto-append mode)  
- Technician name dropdown and validation  
- Local storage for offline use (no internet connection required)  
- Optional email notification when a cut is submitted  

---

## Tech Stack

| Component | Description |
|------------|--------------|
| **Python 3.x** | Core application logic |
| **Tkinter** | Graphical user interface |
| **pandas / openpyxl** | Excel file handling and data export |
| **os / datetime** | File system and timestamp utilities |
| **smtplib (optional)** | Email notification integration |

---

## Installation

### 1. Clone this repository
```bash
git clone https://github.com/chrisrivero-dev/ScanMapsApp.git
cd ScanMapsApp
