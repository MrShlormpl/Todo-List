import tkinter as tk
from TODO_handler import todo_handler


class todo_root():
    def __init__(self, SIZE=(400, 500), file_path=""):

        self.file_path = file_path

        self.root = tk.Tk()
        self.root.title("TODO List")
        self.root.geometry(f"{SIZE[0]}x{SIZE[1]}")
        self.root.configure(bg='lightgray')

        self.entry_widget = tk.Text(
            self.root, 
            height=1, 
            width=48,
            pady=16
        )
        self.entry_widget.bind("<Key>", self.on_key_press)
        self.entry_widget.pack(side='bottom')

        self.button_widget = tk.Button(
            self.root, 
            height=2, 
            width=50,
            text='Add TODO',
            command=self.on_add_click)
        self.button_widget.pack(side='bottom')


        # Implementing TODO frame
        self.canvas = tk.Canvas(self.root, bg="lightgray", highlightthickness=0)
        self.scrollbar = tk.Scrollbar(self.root, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)

        # Create frame inside canvas to hold todo items
        self.todo_frame = tk.Frame(self.canvas, bg="lightgray")
        self.canvas.create_window((0, 0), window=self.todo_frame, anchor="nw")

        # Bind to resize canvas scroll region
        self.todo_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        # Optional mouse wheel scrolling
        self.canvas.bind_all("<MouseWheel>", lambda e: self.canvas.yview_scroll(int(-1*(e.delta/120)), "units"))



        self._todo_handler = todo_handler(self.todo_frame)        
        todos = self.file_read(self.file_path)
        
        for text in todos:
            self.add_todo(text)


    def file_read(self, file_path):
        try:
            with open(file_path, 'r') as file:
                content = file.read()
                content = content.split("\n")
                
                return content

        except FileNotFoundError:
            print(f"Error: The file '{file_path}' was not found.")
            return []
        except Exception as e:
            print(f"An error occurred: {e}")
            return []
        

    def file_write(self, file_path, todo_text):
        try:
            with open(file_path, 'w') as file:
                file.write(todo_text)
                
        except FileNotFoundError:
            print(f"Error: The file '{file_path}' was not found.")
            return []
        except Exception as e:
            print(f"An error occurred: {e}")
            return []



    def on_key_press(self, event):
        if event.keycode == 13:
            self.on_add_click()



    def on_add_click(self):
        
        temp_text = self.entry_widget.get("1.0", "end-1c")

        self.add_todo(temp_text)

        self.entry_widget.delete("1.0", "end-1c")


    def add_todo(self, text):
        if text.strip() == "":
            return
        elif text[0] == '\n':
            self._todo_handler.add_todo(text[1:])
        else:
            self._todo_handler.add_todo(text)


    def mainloop(self):
        
        self.root.mainloop()

        todos = self._todo_handler.get_todos()

        todo_text = "\n".join(todos)

        self.file_write(self.file_path, todo_text)



        # for frame in self._todo_handler.get_frames():
        #     continue
        #     # print(frame.get_text())
        # print("TODO: Implement file writting")
        
        