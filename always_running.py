import subprocess
import tkinter as tk
from datetime import datetime
import os
from tkinter import messagebox
from tkinter import filedialog

# Define the name of the process to monitor and start

process_name = ""

# Initialize the UI
root = tk.Tk()
root.title("Always Running by Harley")
root.geometry("350x250")

process_label_title = tk.Label(root, text="Process Selection", font=("Arial Bold", 14))
process_label_title.pack()

process_label = tk.Label(root, text="No process selected", fg="gray", font=("Arial", 12))
process_label.pack(pady=5)

def select_process():
    global process_name
    process_name = filedialog.askopenfilename()
    process_label.config(text=process_name, fg="black")

process_button = tk.Button(root, text="Select Process", command=select_process)
process_button.pack(pady=5)

status_label_title = tk.Label(root, text="Script Status", font=("Arial Bold", 14))
status_label_title.pack()

status_label = tk.Label(root, text="Script is running", fg="green", font=("Arial", 12))
status_label.pack(pady=5)

# Open the log file for writing
# CHANGE this to where the log file is made and stored.
log_file_path = "C:/always_running_log.txt"
if not os.path.exists(log_file_path):
    open(log_file_path, 'w').close()
log_file = open(log_file_path, "a")

def check_process():
    global process_name
    if process_name == "":
        status_label.config(text="No process selected", fg="gray")
        root.after(10000, check_process)
        return

    # Check if the process is running
    running = False
    for proc in subprocess.Popen("tasklist", stdout=subprocess.PIPE).stdout:
        if process_name.encode() in proc:
            running = True
            break

    # If the process is not running, start it
    if not running:
        # Kill any existing instances of the process
        subprocess.call(['taskkill', '/F', '/T', '/IM', process_name])
        # Start the process
        subprocess.Popen(process_name)
        # Update the UI status label
        status_label.config(text="Script restarted", fg="orange")
        # Log the restart to the log file
        log_file.write("Process restarted at: " + str(datetime.now()) + "\n")
        log_file.flush() # Force the log to be written to the file
    else:
        # Update the UI status label
        status_label.config(text="Script is running", fg="green")

    # Check again after 10 seconds
    root.after(10000, check_process)

# Function to open the log file
def open_log_file():
    os.startfile(log_file_path)

# Function to stop the process and close the application
def stop_process():
    # Ask the user for confirmation
    confirm = messagebox.askquestion("Stop Script", "Are you sure you want to stop the script?")
    if confirm == 'yes':
        # Stop the process
        subprocess.call(['taskkill', '/F', '/T', '/IM', process_name])
        # Update the UI status label
        status_label.config(text="Script stopped", fg="red")
        # Log the stop to the log file
        log_file.write("Process stopped at: " + str(datetime.now()) + "\n")
        log_file.flush() # Force the log to be written to the file
        # Close the application
        root.destroy

    # Check again after 10 seconds
    root.after(10000, check_process)

# Function to open the log file
def open_log_file():
    os.startfile(log_file_path)

# Function to stop the process and close the application
def stop_process():
    # Ask the user for confirmation
    confirm = messagebox.askquestion("Stop Script", "Are you sure you want to stop the script?")
    if confirm == 'yes':
        # Stop the process
        subprocess.call(['taskkill', '/F', '/T', '/IM', process_name])
        # Update the UI status label
        status_label.config(text="Script stopped", fg="red")
        # Log the stop to the log file
        log_file.write("Process stopped at: " + str(datetime.now()) + "\n")
        log_file.flush() # Force the log to be written to the file
        # Close the application
        root.destroy()

# Create the button to open the log file
open_log_button = tk.Button(root, text="Open Log File", command=open_log_file)
open_log_button.pack(pady=5)

# Create the button to stop the process and close the application
stop_button = tk.Button(root, text="Stop programme", bg="red", command=stop_process)
stop_button.pack(pady=5)

# Start checking the process
root.after(0, check_process)

# Start the UI main loop
root.mainloop()

# Close the log file when the script ends
log_file.close()
