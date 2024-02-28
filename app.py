import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("My App")
        self.geometry("300x200")

        self.label = ttk.Label(self, text="Hello, world!")
        self.label.pack(pady=10)

        self.button = ttk.Button(
            self, text="Click me!", command=self.on_button_click)
        self.button.pack()

    def on_button_click(self):
        self.label["text"] = "Button clicked!"


if __name__ == "__main__":
    app = App()
    app.mainloop()
