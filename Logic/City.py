from Logic import StringConstants

class City:
    def __init__(self, view, model):
        self.view = view
        self.view.set_listener(self.change)
        self.model = model
        self.gameOver = False

    def change(self, which_btn):
        if which_btn == "adv":
            try:
                if self.model.bushels >= (
                        int(self.view.inp_plant.get()) + int(self.view.inp_buy.get()) + int(self.view.inp_feed.get())):
                    if ( (self.model.population *10)/ int(self.view.inp_plant.get())) < 1:
                        self.view.info_text.set("You do not have enough people for your acres")
                    elif self.model.year < 11:
                        self.advance_next_year()
                    else:
                        self.game_is_over()
                else:
                    self.view.info_text.set("You do not have enough bushels")
            except ValueError:
                self.view.info_text.set("Please enter a whole number")
        else:
            print("Button?")

    def advance_next_year(self):
        feed = int(self.view.inp_feed.get())
        buy_or_sell = int(self.view.inp_buy.get())
        plant = int(self.view.inp_plant.get())

        self.feed_people(feed)
        self.buy_or_sell_acres(buy_or_sell)
        self.plant_seeds(plant)
        self.model.year = self.model.year + 1
        self.model.update_randoms()
        self.update_gui()

        # self.resetOutput()
        # self.peopleFeed(feed)
        # self.calc_bushels_per_acre(feed)
        # self.harvest(plant)
        # self.calculateAcres(int(buy_or_sell))
        # self.rats()
        # self.disease()
        # self.immigration()
        # self.year += 1

    def feed_people(self, feed):
        needed_food = self.model.population * 20
        if needed_food > feed:
            new_population = int(feed / 20)
            self.model.starved = self.model.population - new_population
            self.model.population = new_population

        self.model.bushels = self.model.bushels - feed
        self.check_if_game_over()

    def buy_or_sell_acres(self, amount):
        self.model.bushels = self.model.bushels + amount * self.model.cost_per_acre
        self.model.acres = self.model.acres + amount

    def plant_seeds(self, plant):
        self.model.acres_with_seeds = self.model.acres_with_seeds + plant
        self.model.bushels = self.model.bushels - plant

    def update_gui(self):
        self.view.year.set(StringConstants.LBL_YEAR + str(self.model.year))
        self.view.starved.set(str(self.model.starved) + StringConstants.LBL_STARVED)
        self.view.immigrants.set(StringConstants.LBL_IMMIGRANTS + str(self.model.immigrants))
        self.view.population.set(StringConstants.LBL_POPULATION + str(self.model.population))
        self.view.harvest_per_acre.set(StringConstants.LBL_HARV_P_ACRE + str(self.model.harvest_per_acre))
        self.view.bushels.set(StringConstants.LBL_BUSHELS + str(self.model.bushels))
        self.view.rats.set(str(self.model.rats) + StringConstants.LBL_RATS)
        self.view.acres.set(StringConstants.LBL_ACRES + str(self.model.acres))
        self.view.cost_acre.set(StringConstants.LBL_COST_P_ACRE + str(self.model.cost_per_acre))
        self.view.plague.set(str(self.model.plague) + StringConstants.LBL_PLAGUE)
        self.view.info_text.set("Long live the Hammurabi")

    def check_if_game_over(self):
        if self.model.population < 1:
            self.game_is_over()

    def game_is_over(self):
        self.view.info_text.set("Game Over")

    def start(self):
        self.view.show()
