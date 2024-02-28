from tkinter import *
from itertools import cycle

class loading(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("400x150+500+300")
        self.screen()
        self.mainloop()

    def screen(self):
        self.resizable(False, False)
        self.title("Student Management System - Loading")
        self.config(background="white")

        title_label = Label(text="Student Management System", font=("Arial", 16, "bold"), background="white")
        title_label.pack(pady=5)

        self.loading_label = Label(font=("Arial", 12), background="white")
        self.loading_label.pack()

        self.loading_animation = cycle(['|', '/', '-', '\\'])  # Symbols for animation
        self.animate()
        self.after(2000, self.destroy)  # Stop after 2 seconds

    def animate(self):
        symbol = next(self.loading_animation)
        self.loading_label.config(text=symbol, fg=self.get_color(symbol), font=("Arial", 16, "bold"), padx=20)
        self.after(200, self.animate)  # Change the delay to adjust animation speed

    def get_color(self, symbol):
        if symbol == '|':
            return 'red'
        elif symbol == '/':
            return 'blue'
        elif symbol == '-':
            return 'green'
        else:
            return 'black'

if __name__ == "__main__":
    l = loading()
