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
                    self.view.info_text.set("As you wish")
                    if self.model.year < 11:
                        self.advance_next_year()
                    else:
                        self.game_is_over()
                else:
                    self.view.info_text.set("You do not have enough bushels")
            except ValueError:
                self.view.info_text.set("Please enter a whole number")
                print("That's not an int!")
        else:
            print("Button?")

    def advance_next_year(self):
        pass

    def check_if_game_over(self):
        pass

    def game_is_over(self):
        pass

    def start(self):
        self.view.show()
