import tkinter as tk

class View():
    def __init__(self, master, controller):
        self.master = master
        self.controller = controller

        self.lbl_acre_amount = None
        self.lbl_feed_people = None
        self.lbl_store = None
        self.btn_play = None

        self.draw_gui()

    def draw_gui(self):
        self.lbl_acre_amount = tk.Label(self.master, text="Amount Acre:")
        self.lbl_acre_amount.pack()

