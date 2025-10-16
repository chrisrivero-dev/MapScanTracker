"""
ScanMapsApp
-----------
Local desktop application for logging and tracking completed Assessor map scans.
Developed by Christopher Rivero – Orange County Assessor’s Office, Mapping Division.

Features:
- Tkinter-based GUI for quick data entry
- Dropdown menu for technician names
- Dropdown for software used (ArcGIS Pro / MicroStation)
- Automatic timestamp logging
- Exports to Excel (Scan_Logs.xlsx)
- Append mode (no data overwrite)
- Status bar feedback and field validation

Dependencies:
    pip install pandas openpyxl
"""

import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
from datetime import datetime
import os

# ---------------------- CONFIGURATION ----------------------

# Excel file name
EXCEL_FILE = "Scan_Logs.xlsx"

# Technician dropdown values
TECHNICIANS = [
    "C. Rivero",
    "E. Delgado",
    "M. Flores",
    "T. Nguyen",
    "D. Martinez"
]

# Software dropdown values
SOFTWARES = [
    "ArcGIS Pro",
    "MicroStation",
    "Other"
]

# -----------------------------------------------------------


class ScanMapsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Scan Maps Completion App")
        self.root.geometry("520x360")
        self.root.resizable(False, False)

        self.create_ui()
        self.create_excel_if_not_exists()

    def create_ui(self):
        # Header
        header = tk.Label(
            self.root,
            text="Scan Maps Completion Logger",
            font=("Helvetica", 16, "bold"),
            pady=10
        )
        header.pack()

        # Frame container
        frame = tk.Frame(self.root, padx=20, pady=10)
        frame.pack(fill="both", expand=True)

        # Cut number
        tk.Label(frame, text="Cut Number:", font=("Helvetica", 11)).grid(row=0, column=0, sticky="e", pady=5)
        self.cut_number_entry = tk.Entry(frame, width=25)
        self.cut_number_entry.grid(row=0, column=1, padx=10, pady=5)

        # Technician
        tk.Label(frame, text="Technician:", font=("Helvetica", 11)).grid(row=1, column=0, sticky="e", pady=5)
        self.tech_var = tk.StringVar()
        self.tech_combo = ttk.Combobox(frame, textvariable=self.tech_var, values=TECHNICIANS, state="readonly", width=22)
        self.tech_combo.grid(row=1, column=1, padx=10, pady=5)
        self.tech_combo.set("Select technician")

        # Software used
        tk.Label(frame, text="Software Used:", font=("Helvetica", 11)).grid(row=2, column=0, sticky="e", pady=5)
        self.software_var = tk.StringVar()
        self.software_combo = ttk.Combobox(frame, textvariable=self.software_var, values=SOFTWARES, state="readonly", width=22)
        self.software_combo.grid(row=2, column=1, padx=10, pady=5)
        self.software_combo.set("Select software")

        # Submit button
        submit_btn = tk.Button(
            frame,
            text="Submit Entry",
            font=("Helvetica", 11, "bold"),
            bg="#0078D7",
            fg="white",
            padx=10,
            pady=5,
            width=20,
            command=self.submit_entry
        )
        submit_btn.grid(row=3, column=0, columnspan=2, pady=15)

        # Status bar
        self.status_label = tk.Label(self.root, text="Ready", bd=1, relief="sunken", anchor="w")
        self.status_label.pack(fill="x", side="bottom", ipady=3)

    def create_excel_if_not_exists(self):
        """Create Excel log file if not already present."""
        if not os.path.exists(EXCEL_FILE):
            df = pd.DataFrame(columns=["Cut Number", "Technician", "Software Used", "Date", "Time"])
            df.to_excel(EXCEL_FILE, index=False)
            print(f"Created {EXCEL_FILE}")

    def submit_entry(self):
        """Validate and log form input to Excel."""
        cut_number = self.cut_number_entry.get().strip()
        technician = self.tech_var.get()
        software = self.software_var.get()

        if not cut_number:
            messagebox.showerror("Error", "Please enter a cut number.")
            return
        if technician == "Select technician":
            messagebox.showerror("Error", "Please select a technician.")
            return
        if software == "Select software":
            messagebox.showerror("Error", "Please select a software type.")
            return

        now = datetime.now()
        date = now.strftime("%Y-%m-%d")
        time = now.strftime("%I:%M %p")

        # Prepare new entry
        new_entry = pd.DataFrame(
            [[cut_number, technician, software, date, time]],
            columns=["Cut Number", "Technician", "Software Used", "Date", "Time"]
        )

        # Append to Excel
        try:
            if os.path.exists(EXCEL_FILE):
                existing_df = pd.read_excel(EXCEL_FILE)
                df = pd.concat([existing_df, new_entry], ignore_index=True)
            else:
                df = new_entry
            df.to_excel(EXCEL_FILE, index=False)

            self.status_label.config(text=f"Logged cut #{cut_number} successfully ✅")
            messagebox.showinfo("Success", f"Entry for cut #{cut_number} saved successfully!")
            self.clear_form()

        except Exception as e:
            messagebox.showerror("Error", f"Failed to save entry.\n\n{e}")

    def clear_form(self):
        """Reset form fields."""
        self.cut_number_entry.delete(0, tk.END)
        self.tech_combo.set("Select technician")
        self.software_combo.set("Select software")


# ---------------------- RUN APP ----------------------

if __name__ == "__main__":
    root = tk.Tk()
    app = ScanMapsApp(root)
    root.mainloop()
