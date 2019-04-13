from Logic import City
from Logic import View
from Logic import Model

model = Model.Model()
view = View.View()
city = City.City(view, model)

city.start()