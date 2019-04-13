import tkinter as tk
from Logic import StringConstants

class View:
    def __init__(self):
        self.listener = None

        self.window = tk.Tk()
        self.window.geometry("800x400")
        self.window.title(StringConstants.TITLE)

        self.year = tk.StringVar()
        self.lbl_year = tk.Label(self.window, textvariable=self.year)
        self.lbl_year.grid(row=0, column=0, sticky="W")

        self.starved = tk.StringVar()
        self.lbl_starved = tk.Label(self.window, textvariable=self.starved)
        self.lbl_starved.grid(row=1, column=0, sticky="W")

        self.immigrants = tk.StringVar()
        self.lbl_immigrants = tk.Label(self.window, textvariable=self.immigrants)
        self.lbl_immigrants.grid(row=2, column=0, sticky="W")

        self.population = tk.StringVar()
        self.lbl_population = tk.Label(self.window, textvariable=self.population)
        self.lbl_population.grid(row=3, column=0, sticky="W")

        self.harvest_per_acre = tk.StringVar()
        self.lbl_harvest_per_acre = tk.Label(self.window, textvariable=self.harvest_per_acre)
        self.lbl_harvest_per_acre.grid(row=4, column=0, sticky="W")

        self.bushels = tk.StringVar()
        self.lbl_bushels = tk.Label(self.window, textvariable=self.bushels)
        self.lbl_bushels.grid(row=5, column=0, sticky="W")

        self.rats = tk.StringVar()
        self.lbl_rats = tk.Label(self.window, textvariable=self.rats)
        self.lbl_rats.grid(row=6, column=0, sticky="W")

        self.acres = tk.StringVar()
        self.lbl_acres = tk.Label(self.window, textvariable=self.acres)
        self.lbl_acres.grid(row=7, column=0, sticky="W")

        self.cost_acre = tk.StringVar()
        self.lbl_cost_acre = tk.Label(self.window,
                                      textvariable=self.cost_acre)
        self.lbl_cost_acre.grid(row=8, column=0, sticky="W")

        self.plague = tk.StringVar()
        self.lbl_plague = tk.Label(self.window, textvariable=self.plague)
        self.lbl_plague.grid(row=9, column=0, sticky="W")

        self.lbl_buy = tk.Label(self.window, text=StringConstants.LBL_BUY_SELL)
        self.lbl_buy.grid(row=11, column=0, sticky="W")
        self.inp_buy = tk.Entry(self.window)
        self.inp_buy.grid(row=11, column=1, sticky="W")

        self.feed_info = tk.StringVar()
        self.lbl_feed = tk.Label(self.window, textvariable=self.feed_info)
        self.lbl_feed.grid(row=12, column=0, sticky="W")
        self.inp_feed = tk.Entry(self.window)
        self.inp_feed.grid(row=12, column=1, sticky="W")

        self.lbl_plant = tk.Label(self.window, text=StringConstants.LBL_PLANT)
        self.lbl_plant.grid(row=13, column=0, sticky="W")
        self.inp_plant = tk.Entry(self.window)
        self.inp_plant.grid(row=13, column=1, sticky="W")

        self.btn_advance = tk.Button(self.window, text=StringConstants.BTN_ADVANCE,
                                     command=lambda: self.change("adv"))
        self.btn_advance.grid(row=14)

        self.info_text = tk.StringVar()
        self.lbl_info = tk.Label(self.window, textvariable=self.info_text)
        self.lbl_info.grid(row=15)

    def set_listener(self, listener):
        self.listener = listener

    def change(self, which_btn):
        if self.listener:
            self.listener(which_btn)

    def show(self):
        self.window.mainloop()
