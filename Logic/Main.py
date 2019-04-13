from Logic import City
from Logic import View
from Logic import Model

view = View.View()
model = Model.Model()
city = City.City(view, model)

city.start()