import tkinter as tk
from tkinter import ttk
from modules import loading_screen, login_screen


# home window
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1200x800")
        self.title("Student Management System")
        login_screen.Login(self)


if __name__ == "__main__":
    loading_screen.Loading()
    g = App()
    g.mainloop()
