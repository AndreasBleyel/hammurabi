import unittest

from Logic import City
from Logic import Model
from Logic import View


class CityTest(unittest.TestCase):

    def setUp(self):
        self.view = View.View()
        self.model = Model.Model()
        self.city = City.City(self.view, self.model)

    def test_too_less_feeding(self):
        self.assertEqual(self.city.calc_min_needed_food(), 2000)

    def test_too_less_acres_to_sell(self):
        self.view.inp_buy.insert(0, "-100")
        self.model.acres = 50
        self.assertFalse(self.city.check_if_enough_acres_to_sell())

    def test_enough_acres_to_sell(self):
        self.view.inp_buy.insert(0, "-100")
        self.model.acres = 150
        self.assertTrue(self.city.check_if_enough_acres_to_sell())

    def test_too_less_bushels_to_buy(self):
        self.view.inp_buy.insert(0, "100")
        self.view.inp_feed.insert(0, "500")
        self.view.inp_plant.insert(0, "400")
        self.model.bushels = 500
        self.assertFalse(self.city.check_if_enough_bushels())

    def test_enough_bushels_to_buy(self):
        self.view.inp_buy.insert(0, "100")
        self.view.inp_feed.insert(0, "500")
        self.view.inp_plant.insert(0, "400")
        self.model.cost_per_acre = 10
        self.model.bushels = 2000
        self.assertTrue(self.city.check_if_enough_bushels())

    def test_enough_bushels_to_buy_negative_input(self):
        self.view.inp_buy.insert(0, "-100")
        self.view.inp_feed.insert(0, "500")
        self.view.inp_plant.insert(0, "400")
        self.model.cost_per_acre = 10
        self.model.bushels = 2000
        self.assertTrue(self.city.check_if_enough_bushels())

    def test_too_less_people_to_plant(self):
        self.model.population = 10
        self.view.inp_plant.insert(0, "400")
        self.assertFalse(self.city.check_if_enough_people_for_plant())

    def test_enough_people_to_plant(self):
        self.model.population = 100
        self.view.inp_plant.insert(0, "400")
        self.assertTrue(self.city.check_if_enough_people_for_plant())

    def test_too_less_acres_to_plant(self):
        self.model.acres = 500
        self.view.inp_plant.insert(0, "600")
        self.assertFalse(self.city.check_if_enough_acres_to_plant())

    def test_enough_acres_to_plant(self):
        self.model.acres = 600
        self.view.inp_plant.insert(0, "600")
        self.assertTrue(self.city.check_if_enough_acres_to_plant())

    def test_reset_done(self):
        self.city.reset_for_next_year()
        self.assertEqual(self.model.starved, 0)
        self.assertEqual(self.model.immigrants, 0)
        self.assertEqual(self.model.acres_with_seeds, 0)


if __name__ == '__main__':
    unittest.main()
