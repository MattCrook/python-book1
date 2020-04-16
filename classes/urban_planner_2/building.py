import datetime


class Building:

    def __init__(self, address, stories):
        self.owner = "TBD"
        self.address = address
        self.stories = stories
        self.designer = "Matt Crook"
        self.date_constructed = "Today"

    def construct(self):
        self.date_constructed = datetime.datetime.now

    def purchase(self, buyer):
        self.owner = buyer
