# Always Running
Always Running is a Python script that monitors a specified process and restarts it if it stops running. This is useful for ensuring that critical processes are always running, and can prevent downtime in certain situations.

## Requirements
Always Running requires Python 3 and the Tkinter library, which is included in most Python distributions.

## How to Use
Download the script and save it to your preferred location.
Open a terminal or command prompt and navigate to the directory where the script is saved.
Run the command python always_running.py to start the script.
Select the process you want to monitor by clicking the "Select Process" button and navigating to the process executable.
Click the "Open Log File" button to view the log file, which contains a record of process restarts and stops.
Click the "Stop Program" button to stop the monitoring script and close the application.
Note: Always Running should be run as an administrator to ensure that it has permission to start and stop processes. To run the script as an administrator, right-click on the script and select "Run as administrator" from the context menu.

## How it Works
The script uses the subprocess library to run the tasklist command and check if the specified process is running. If the process is not running, the script uses subprocess to run the taskkill command and kill any existing instances of the process, then uses subprocess again to start the process. The script also logs each process restart and stop to a log file, and updates a status label in the UI to reflect the current state of the process. The UI is built using the tkinter library.

## Running as an Administrator
Always Running should be run as an administrator to ensure that it has permission to start and stop processes. To run the script as an administrator, right-click on the script and select "Run as administrator" from the context menu.
