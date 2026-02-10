import tkinter as tk
from tkinter import messagebox


class _TODO_Frame(tk.Frame):
    def __init__(self, master=None, TODO_text="Default", **kwargs):
        super().__init__(master, **kwargs)

        self._text = TODO_text
        self._is_destroyed = False

        self.config(width=400, height=50, pady=4)
        self.pack_propagate(False)


        self.label = tk.Label(self, text="- "+self._text)
        self.label.pack(side='left',padx=10)

        self.button = tk.Button(self, text="X", command=self.on_click, height=10, width=10, bg='red', fg='white')
        self.button.pack(side='right', padx=10)

        self.pack(side='top')

    def on_click(self):
        response = messagebox.askyesno(
            "Confirmation",
            "Is this task complete?"
        )
        
        if response:
            self.destroy()
            self._is_destroyed = True
        else:
            return
    
    def get_text(self):
        return self._text
    
    def is_destroyed(self):
        return self._is_destroyed
        