import tkinter as tk
from Logic import View as view, StringConstants


class Main:
    def __init__(self):
        self.tk = tk.Tk()
        self.view = view.View(self.tk, self)
        self.initGui()

    def initGui(self):
        self.tk.geometry("600x400")
        self.tk.title(StringConstants.TITLE)

    def run(self):
        self.tk.mainloop()


game = Main()
game.run()
