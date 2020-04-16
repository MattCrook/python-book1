from building import Building
from city import City


building_1 = Building("123 street", 30)
building_1.purchase("Joe Shmoe")
building_1.construct()

building_2 = Building("987 street", 50)
building_2.purchase("Big Mike")
building_2.construct()

building_3 = Building("456 avenue", 80)
building_3.purchase("Moe Mogul")
building_3.construct()

print(building_1)
