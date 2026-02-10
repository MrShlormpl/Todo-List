import TODO_root as tdr
import os

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the absolute path to your text file
FILE_NAME = os.path.join(script_dir, 'TODO.txt')


root = tdr.todo_root(file_path=FILE_NAME)

root.mainloop()