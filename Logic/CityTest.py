import unittest
import random

from Logic import City as city
class CityTest(unittest.TestCase):

    def setUp(self):
        self.city = city.City()

    def test_too_less_bushes(self):
        pass


if __name__ == '__main__':
    unittest.main()