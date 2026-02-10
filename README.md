# Python TODO List #

This python application is designed to help you keep track of any tasks you may have. It works by being linked to the Task Scheduler so it may run whenever you turn on your Windows device.

## How to set up.

1. Open Task Scheduler
2. Find the folder in the Task Scheduler Library where you want to store the task (I created my own folder for this)
3. While selecting your folder, select 'Create Task' 
4. In the 'General' tab, name this task whatever you like
5. In the 'Triggers' tab, add a new trigger 'On workstation unlock' (of any user or a selected user)
6. In the 'Actions' Tab, add a new action for 'Start a program'. For the program, enter in the address for your python compiler (Note: Use 'pythonw.exe' if you wish to hide the terminal). For your arguments, enter the address of 'TODO.py', surrounded by quotation marks.
7. Save the task, and you should have the TODO list set up!


*Note: This is just how I have it implemented. You're more than welcome to convert this into a .exe file and run it manually. 
