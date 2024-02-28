from tkinter import *
from itertools import cycle

class Loading(Tk):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.geometry("400x150+500+300")
        self.createWidgets()
        self.mainloop()

    def createWidgets(self):
        self.resizable(False, False)
        self.title("Student Management System - Loading")

        # Using pack layout manager for simplicity and central alignment
        self.title_label = Label(self, text="Student Management System", font=("Arial", 16, "bold"))
        self.title_label.pack(pady=5)

        self.loading_label = Label(self, font=("Arial", 12))
        self.loading_label.pack(pady=10)  # Increased padding for a cleaner look

        self.loading_animation = cycle(['|', '/', '-', '\\'])  # Symbols for animation
        self.animate()
        self.after(2000, self.destroy)  # Stop after 2 seconds

    def animate(self):
        symbol = next(self.loading_animation)
        # Removed get_color function and fixed the font and color to black for simplicity
        self.loading_label.config(text=symbol, font=("Arial", 16, "bold"))
        self.after(200, self.animate)  # Change the delay to adjust animation speed

if __name__ == "__main__":
    Loading()
