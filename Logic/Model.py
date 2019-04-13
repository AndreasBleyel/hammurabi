from Logic import Randoms

class Model:
    def __init__(self):
        self.year = 1
        self.starved = 0
        self.immigrants = 0
        self.population = 100
        self.harvest_per_acre = Randoms.RND_HARVEST
        self.bushels = 2800
        self.rats = Randoms.RND_RATS
        self.acres = 1000
        self.cost_per_acre = Randoms.RND_TRADE
        self.plague = Randoms.RND_PLAGUE
        self.acres_with_seeds = 0

        self.buy_or_sell = 0
        self.feed = 0
        self.plant = 0

    def calc_population(self):
        self.population = self.bushels / 20

    def update_randoms(self):
        self.harvest_per_acre = Randoms.RND_HARVEST
        self.rats = Randoms.RND_RATS
        self.cost_per_acre = Randoms.RND_TRADE
        self.plague = Randoms.RND_PLAGUE
