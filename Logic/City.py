from Logic import StringConstants


class City:
    def __init__(self, view, model):
        self.view = view
        self.view.set_listener(self.change)
        self.model = model
        self.game_over = False
        self.someone_died = False

    def change(self, which_btn):
        """ Click Listener. Führt Logik gemäß geklicktem Button aus.
            Advance - Prüfen ob Eingaben korrekt und erst dann wird mit der Jahresabrechnung
            begonnen.
            Restart - setzt Model und relevante Spielparameter zurück und startet das Spiel
            neu
        """
        if which_btn == "adv":
            try:
                if self.check_if_enough_bushels():
                    if not self.check_if_enough_people_for_plant():
                        self.view.info_text.set("You do not have enough people for your acres")
                    elif not self.check_if_enough_acres_to_plant():
                        self.view.info_text.set("You do not have enough acres to plant that much")
                    elif self.model.year < 11:
                        if int(self.view.inp_buy.get()) < 0:
                            if self.check_if_enough_acres_to_sell():
                                self.advance_next_year()
                            else:
                                self.view.info_text.set("You do not have enough acres to sell")
                        else:
                            self.advance_next_year()
                    else:
                        self.game_is_over()
                else:
                    self.view.info_text.set("You do not have enough bushels")
            except ValueError:
                self.view.info_text.set("Please enter a whole number")
                print(int(self.view.inp_buy.get()))
        else:
            self.restart()

    def advance_next_year(self):
        """ Jahr abschließen und neues starten.
            Reihenfolge: 1) Leute füttern 2) Ackerland verkaufen/kaufen
            3) Acker bestellen
            Neue Randoms berechnen
            Bushels und Population gemäß Eingaben berechnen
            Jahreszahl erhöhen
            GUI anpassen und prüfen ob Spielende erreicht
        """
        feed = int(self.view.inp_feed.get())
        buy_or_sell = int(self.view.inp_buy.get())
        plant = int(self.view.inp_plant.get())

        self.model.update_randoms()
        self.feed_people(feed)
        self.buy_or_sell_acres(buy_or_sell)
        self.plant_seeds(plant)
        self.calc_bushels()
        self.calc_population()
        self.model.year = self.model.year + 1
        self.update_gui()
        self.reset_for_next_year()
        self.check_if_game_over()

    def feed_people(self, feed):
        """ Prüfen ob genug Futter bereitgestellt wurde. Falls nicht, Population an
        bereitgestellte Menge anpassen
        """
        if self.calc_min_needed_food() > feed:
            new_population = int(feed / 20)
            self.model.starved = self.model.population - new_population
            self.model.population = new_population
            self.someone_died = True
        else:
            self.someone_died = False

        self.model.bushels = self.model.bushels - feed

    def buy_or_sell_acres(self, amount):
        """ Ackerland gemäß Eingabe kaufen/verkaufen """
        self.model.bushels = self.model.bushels - amount * self.model.cost_per_acre
        self.model.acres = self.model.acres + amount

    def plant_seeds(self, plant):
        """ Ackerland gemäß Eingabe bestellen"""
        self.model.acres_with_seeds = plant
        self.model.bushels = self.model.bushels - plant

    def calc_bushels(self):
        """ Ertrag an Bushels abzüglich gefressener (Ratten) berechnen """
        self.model.bushels = self.model.bushels + self.model.acres_with_seeds * self.model.harvest_per_acre
        self.model.bushels = self.model.bushels - self.model.rats

    def calc_population(self):
        """ Population nach Fütterung mit Verlusten aus Plagen abgleichen.
            Wenn niemand durch Hunger gestorben ist, zufällige Immigranten
            hinzuaddieren
        """
        self.model.population = self.model.population - self.model.plague
        if not self.someone_died:
            self.model.calc_immigrants()
            self.model.population = self.model.population + self.model.immigrants

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
        self.view.feed_info.set(StringConstants.LBL_FEED + str(self.calc_min_needed_food()))
        self.view.info_text.set("Long live the Hammurabi")

    def calc_min_needed_food(self):
        """ Mindestmenge an benötigtem Futter (20/Person) """
        return self.model.population * 20

    def check_if_enough_acres_to_sell(self):
        """ Prüfen ob gewünschte Anzahl an zu verkaufendem Ackerland überhaupt
            in Besitz ist
        """
        return True if self.model.acres >= (int(self.view.inp_buy.get()) * -1) else False

    def check_if_enough_bushels(self):
        """ Prüfen ob genug Bushels für gewünschte Aktionen überhaupt
            verfügbar ist
        """
        if int(self.view.inp_buy.get()) > 0:
            return True if self.model.bushels >= (
                    int(self.view.inp_plant.get()) + (int(self.view.inp_buy.get()) * self.model.cost_per_acre) + int(
                self.view.inp_feed.get())) else False
        else:
            return True if self.model.bushels >= (
                    int(self.view.inp_plant.get()) + int(self.view.inp_feed.get())) else False

    def check_if_enough_people_for_plant(self):
        """ Prüfen ob genügend Leute zur Bestellung der gewünschten Anzahl
            an Feldern vorhanden
        """
        if int(self.view.inp_plant.get()) > 0:
            return True if ((self.model.population * 10) / int(self.view.inp_plant.get())) >= 1 else False
        else:
            return True

    def check_if_enough_acres_to_plant(self):
        """ Prüfen ob genügend Felder zur Bestellung der gewünschten Anzahl
            vorhanden ist
        """
        return True if self.model.acres >= int(self.view.inp_plant.get()) else False

    def reset_for_next_year(self):
        """" Eingabefelder und Rundenbasierte Felder zurücksetzen """
        self.model.acres_with_seeds = 0
        self.view.inp_feed.delete(0, "end")
        self.view.inp_buy.delete(0, "end")
        self.view.inp_plant.delete(0, "end")
        self.model.starved = 0
        self.model.immigrants = 0

    def check_if_game_over(self):
        """ Prüfen ob Spiel zu Ende. Bei Erreichen von 0 Population
            oder 0 Bushels
        """
        if self.model.population < 1 or self.model.bushels < 1:
            self.game_is_over()

    def game_is_over(self):
        """ Berechnen der Highscore nach Spielende """
        total_score = self.model.population * 100 + self.model.bushels
        self.view.info_text.set("Game Over! Your total Score: " + str(total_score))

    def restart(self):
        """" Rücksetzen aller Parameter und GUI zum Neustart """
        self.model.update_randoms()
        self.model.set_to_start_vals()
        self.view.inp_feed.delete(0, "end")
        self.view.inp_buy.delete(0, "end")
        self.view.inp_plant.delete(0, "end")
        self.game_over = False
        self.someone_died = False
        self.update_gui()

    def start(self):
        self.update_gui()
        self.view.show()
