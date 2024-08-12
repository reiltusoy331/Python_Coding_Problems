import tkinter as tk
from tkinter import filedialog

def browse_for_csv():
    # Create a Tkinter root window
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Open a file dialog and filter to show only CSV files
    file_path = filedialog.askopenfilename(
        filetypes=[("CSV files", "*.csv")],
        title="Select a CSV file"
    )

    if file_path:
        print(f"Selected file: {file_path}")
    else:
        print("No file selected")

if __name__ == "__main__":
    browse_for_csv()
