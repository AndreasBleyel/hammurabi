import unittest
import random

from Logic import City as city
class CityTest(unittest.TestCase):

    def setUp(self):
        self.city = city.City()

    def test_too_less_feeding(self):

        self.city.feed_people()


if __name__ == '__main__':
    unittest.main()