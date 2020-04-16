import datetime


class Building:

    def __init__(self, name, address, stories):
        self.name = name
        self.owner = "TBD"
        self.address = address
        self.stories = stories
        self.designer = "Matt Crook"
        self.date_constructed = "Today"

    def construct(self):
        self.date_constructed = datetime.datetime.now()

    def purchase(self, buyer):
        self.owner = buyer

    def show_details(self):
        company = self.__dict__
        for prop, value in company.items():
            print(f'{prop}:\n{value}\n')
