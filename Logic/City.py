import random
from Logic import StringConstants
from Logic import Randoms

class City:
    def __init__(self, view, model):
        self.view = view
        self.view.set_listener(self.change)
        self.model = model
        self.gameOver = False

    def change(self):
        pass

    def start(self):
        self.view.show()



