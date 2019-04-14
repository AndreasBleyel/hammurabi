import random


class Model:
    def __init__(self):
        self.year = 1
        self.starved = 0
        self.immigrants = 0
        self.population = 100
        self.harvest_per_acre = 0
        self.bushels = 2800
        self.rats = 0
        self.acres = 1000
        self.cost_per_acre = 0
        self.plague = 0
        self.acres_with_seeds = 0

        self.update_randoms()

    def update_randoms(self):
        self.harvest_per_acre = random.randint(2, 10)
        self.rats = random.randint(0, 200)
        self.cost_per_acre = random.randint(17, 26)
        self.plague = random.randint(0, 10)

    def set_to_start_vals(self):
        self.year = 1
        self.starved = 0
        self.immigrants = 0
        self.population = 100
        self.harvest_per_acre = 0
        self.bushels = 2800
        self.rats = 0
        self.acres = 1000
        self.cost_per_acre = 0
        self.plague = 0
        self.acres_with_seeds = 0

    def calc_immigrants(self):
        factor = int(self.population * 0.10)
        self.immigrants = random.randint(0, factor)
