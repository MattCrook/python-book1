import datetime


class Building:
    def __init__(self, address, stories):
        self.address = address
        self.stories = stories
        self.designer = ""
        self.date_constructed = "today"
        self.owner = ""

    def construct(self):
        self.date_constructed = datetime.datetime.now()

    def purchase(self, purchaser_name):
        self.owner = purchaser_name

    def print_details(self):
        building = self.__dict__
        print(f"{building['address']} was purchased by {building['owner']} on {building['date_constructed']} and has {building['stories']} floors.")


first_building = Building("800 8th street", 12)
first_building.owner = "Matt"
first_building.purchase("Major Mogul Steve")
first_building.construct()
first_building.print_details()
'''800 8th street was purchased by Major Mogul Steve on 2020-04-14 16:29:38.711797 and has 12 floors.'''


def sell(purchaser):
    buildings = (
        Building("900 9th street", 15),
        Building("500 5th street", 25),
        Building("300 3th street", 30),
        Building("100 1th street", 50)
    )

    for building in buildings:
        building.purchase(purchaser)
        building.construct()
        building.print_details()

sell("Mogul Joe")
sell("Mogol Bob")
sell("Mogul Sean")
sell("Mogul Mike")
