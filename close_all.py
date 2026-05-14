import subprocess
import os
import tkinter as tk
from tkinter import messagebox

current_pid = os.getpid()

# Close all windows except this Python process
subprocess.run(
    ["powershell", "-Command",
     f"Get-Process | Where-Object {{ $_.MainWindowTitle -ne '' -and $_.Id -ne {current_pid} }} | Stop-Process -Force"],
    capture_output=True, text=True
)

# Now ask about shutdown
root = tk.Tk()
root.withdraw()
root.attributes('-topmost', True)

answer = messagebox.askyesno("Shutdown", "Do you want to shutdown the system?")

root.destroy()

if answer:
    subprocess.run(["shutdown", "/s", "/t", "0"])
