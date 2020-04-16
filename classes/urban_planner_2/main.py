from building import Building
from city import City
import datetime


building_1 = Building("Ocean", "123 street", 30)
building_1.purchase("Joe Shmoe")
building_1.construct()

building_2 = Building("Tree", "987 street", 50)
building_2.purchase("Big Mike")
building_2.construct()

building_3 = Building("Mountain", "456 avenue", 80)
building_3.purchase("Moe Mogul")
building_3.construct()

megalopolis = City("megalopolis", "Mayor Matt", "2020")
megalopolis.add_building(building_3)
megalopolis.add_building(building_2)


for building in megalopolis.collection_of_buildings:
    print(building.name)

# Mountain
# Tree
