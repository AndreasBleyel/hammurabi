import tkinter as tk
from Logic import StringConstants
from Logic import Randoms


class View:
    def __init__(self):
        self.listener = None

        self.window = tk.Tk()
        self.window.geometry("600x400")
        self.window.title(StringConstants.TITLE)

        self.lbl_year = tk.Label(self.window, text=StringConstants.LBL_YEAR + " 1")
        self.lbl_year.grid(row=0, column=0, sticky="W")

        self.lbl_starved = tk.Label(self.window, text="0 " + StringConstants.LBL_STARVED)
        self.lbl_starved.grid(row=1, column=0, sticky="W")

        self.lbl_immigrants = tk.Label(self.window, text=StringConstants.LBL_IMMIGRANTS + " 0")
        self.lbl_immigrants.grid(row=2, column=0, sticky="W")
        self.lbl_population = tk.Label(self.window, text=StringConstants.LBL_POPULATION + " 100")
        self.lbl_population.grid(row=3, column=0, sticky="W")
        self.lbl_harvest_per_acre = tk.Label(self.window, text=StringConstants.LBL_HARV_P_ACRE + " 0")
        self.lbl_harvest_per_acre.grid(row=4, column=0, sticky="W")
        self.lbl_bushels = tk.Label(self.window, text=StringConstants.LBL_BUSHELS + " 2800")
        self.lbl_bushels.grid(row=5, column=0, sticky="W")
        self.lbl_rats = tk.Label(self.window, text="0 " + StringConstants.LBL_RATS)
        self.lbl_rats.grid(row=6, column=0, sticky="W")
        self.lbl_acres = tk.Label(self.window, text=StringConstants.LBL_ACRES + " 1000")
        self.lbl_acres.grid(row=7, column=0, sticky="W")
        self.lbl_cost_acre = tk.Label(self.window,
                                      text=StringConstants.LBL_COST_P_ACRE + " " + str(Randoms.RND_TRADE))
        self.lbl_cost_acre.grid(row=8, column=0, sticky="W")
        self.lbl_plague = tk.Label(self.window, text="0 " + StringConstants.LBL_PLAGUE)
        self.lbl_plague.grid(row=9, column=0, sticky="W")

        self.lbl_buy = tk.Label(self.window, text=StringConstants.LBL_BUY_SELL)
        self.lbl_buy.grid(row=11, column=0, sticky="W")
        self.inp_buy = tk.Entry(self.window)
        self.inp_buy.grid(row=11, column=1, sticky="W")

        self.lbl_feed = tk.Label(self.window, text=StringConstants.LBL_FEED)
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

    def get_buy_sell(self):
        return self.inp_buy.get()

    def get_feed(self):
        return self.inp_feed.get()

    def get_plant(self):
        return self.inp_plant.get()

    def show(self):
        self.window.mainloop()
