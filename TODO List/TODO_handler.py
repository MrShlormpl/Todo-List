import tkinter as tk
from tkinter import ttk

from TODO_Frame import _TODO_Frame

class todo_handler(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        
        self.pack(
            side='top',
            fill="both",
            expand=True
            )
        
        self._todo_frames = []

        

    def add_todo(self, text):
        self._todo_frames.append(_TODO_Frame(self, TODO_text=text))

    def get_frames(self):
        # return self._todo_frames
        return [ x for x in self._todo_frames if x.is_destroyed() == False]
    
    def get_todos(self):

        result = []

        for frame in self.get_frames():
            result.append(frame.get_text())
        
        return result