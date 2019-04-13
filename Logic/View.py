import tkinter as tk
from Logic import StringConstants


class View():
    def __init__(self, master, controller):
        self.master = master
        self.controller = controller

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

        self.draw_gui()

    def draw_gui(self):
        self.lbl_year = tk.Label(self.master, text=StringConstants.LBL_YEAR).grid(row=0, column=0, sticky="W")
        self.lbl_starved = tk.Label(self.master, text=StringConstants.LBL_STARVED).grid(row=1, column=0, sticky="W")
        self.lbl_immigrants = tk.Label(self.master, text=StringConstants.LBL_IMMIGRANTS).grid(row=2, column=0,
                                                                                              sticky="W")
        self.lbl_population = tk.Label(self.master, text=StringConstants.LBL_POPULATION).grid(row=3, column=0,
                                                                                              sticky="W")
        self.lbl_harvest_per_acre = tk.Label(self.master, text=StringConstants.LBL_HARV_P_ACRE).grid(row=4, column=0,
                                                                                                     sticky="W")
        self.lbl_bushels = tk.Label(self.master, text=StringConstants.LBL_BUSHELS).grid(row=5, column=0, sticky="W")
        self.lbl_rats = tk.Label(self.master, text=StringConstants.LBL_RATS).grid(row=6, column=0, sticky="W")
        self.lbl_acres = tk.Label(self.master, text=StringConstants.LBL_ACRES).grid(row=7, column=0, sticky="W")
        self.lbl_cost_acre = tk.Label(self.master, text=StringConstants.LBL_COST_P_ACRE).grid(row=8, column=0,
                                                                                              sticky="W")
        self.lbl_plague = tk.Label(self.master, text=StringConstants.LBL_PLAGUE).grid(row=9, column=0, sticky="W")

        self.lbl_buy = tk.Label(self.master, text=StringConstants.LBL_BUY_SELL).grid(row=11, column=0, sticky="W")
        self.inp_buy = tk.Entry(self.master).grid(row=11, column=1, sticky="W")

        self.lbl_feed = tk.Label(self.master, text=StringConstants.LBL_FEED).grid(row=12, column=0, sticky="W")
        self.inp_feed = tk.Entry(self.master).grid(row=12, column=1, sticky="W")

        self.lbl_plant = tk.Label(self.master, text=StringConstants.LBL_PLANT).grid(row=13, column=0, sticky="W")
        self.inp_plant = tk.Entry(self.master).grid(row=13, column=1, sticky="W")

        self.btn_advance = tk.Button(self.master, text=StringConstants.BTN_ADVANCE).grid(row=14)
