import tkinter as tk
from Logic import StringConstants
from Logic import Randoms


class View():
    def __init__(self):
        self.listener = None

        self.window = tk.Tk()
        self.window.geometry("600x400")
        self.window.title(StringConstants.TITLE)

        self.lbl_year = None
        self.lbl_starved = None
        self.lbl_immigrants = None
        self.lbl_population = None
        self.lbl_harvest_per_acre = None
        self.lbl_bushels = None
        self.lbl_rats = None
        self.lbl_acres = None
        self.lbl_cost_acre = None
        self.lbl_plague = None

        self.lbl_buy = None
        self.inp_buy = None

        self.lbl_feed = None
        self.inp_feed = None

        self.lbl_plant = None
        self.inp_plant = None

        self.btn_advance = None

        self.init_gui()

    def init_gui(self):
        self.lbl_year = tk.Label(self.window, text=StringConstants.LBL_YEAR + " 1").grid(row=0, column=0, sticky="W")
        self.lbl_starved = tk.Label(self.window, text="0 " + StringConstants.LBL_STARVED).grid(row=1, column=0,
                                                                                               sticky="W")
        self.lbl_immigrants = tk.Label(self.window, text=StringConstants.LBL_IMMIGRANTS + " 0").grid(row=2, column=0,
                                                                                                     sticky="W")
        self.lbl_population = tk.Label(self.window, text=StringConstants.LBL_POPULATION + " 100").grid(row=3, column=0,
                                                                                                       sticky="W")
        self.lbl_harvest_per_acre = tk.Label(self.window, text=StringConstants.LBL_HARV_P_ACRE + " 0").grid(row=4,
                                                                                                            column=0,
                                                                                                            sticky="W")
        self.lbl_bushels = tk.Label(self.window, text=StringConstants.LBL_BUSHELS + " 2800").grid(row=5, column=0,
                                                                                                  sticky="W")
        self.lbl_rats = tk.Label(self.window, text="0 " + StringConstants.LBL_RATS).grid(row=6, column=0, sticky="W")
        self.lbl_acres = tk.Label(self.window, text=StringConstants.LBL_ACRES + " 1000").grid(row=7, column=0,
                                                                                              sticky="W")
        self.lbl_cost_acre = tk.Label(self.window,
                                      text=StringConstants.LBL_COST_P_ACRE + " " + str(Randoms.RND_TRADE)).grid(
            row=8, column=0,
            sticky="W")
        self.lbl_plague = tk.Label(self.window, text="0 " + StringConstants.LBL_PLAGUE).grid(row=9, column=0,
                                                                                             sticky="W")

        self.lbl_buy = tk.Label(self.window, text=StringConstants.LBL_BUY_SELL).grid(row=11, column=0, sticky="W")
        self.inp_buy = tk.Entry(self.window).grid(row=11, column=1, sticky="W")

        self.lbl_feed = tk.Label(self.window, text=StringConstants.LBL_FEED).grid(row=12, column=0, sticky="W")
        self.inp_feed = tk.Entry(self.window).grid(row=12, column=1, sticky="W")

        self.lbl_plant = tk.Label(self.window, text=StringConstants.LBL_PLANT).grid(row=13, column=0, sticky="W")
        self.inp_plant = tk.Entry(self.window).grid(row=13, column=1, sticky="W")

        self.btn_advance = tk.Button(self.window, text=StringConstants.BTN_ADVANCE,
                                     command=lambda: self.change("advance")).grid(row=14)

    def set_listener(self, listener):
        self.listener = listener

    def change(self, which_btn):
        if self.listener:
            self.listener(which_btn)

    def show(self):
        self.window.mainloop()
