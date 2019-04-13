import tkinter as tk

from Logic import View as view

class Main:
    def __init__(self):
        self.tk = tk.Tk()
        self.view = view.View(self.tk, self)
        self.initGui()

    def initGui(self):
        self.tk.geometry("400x200")
        self.tk.title("Hammurabi")

    def run(self):
        self.tk.mainloop()

game = Main()
game.run()