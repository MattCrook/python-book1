class Pizza:
    def __init__(self):
        self.size = ""
        self.style = ""
        self.toppings = []

    # Add a method for interacting with a pizza's toppings, called add_topping.
    def add_topping(self, topping):
        self.toppings.append(topping)

    # Add a method for outputting a description of the pizza (sample output below).
    def print_order(self):
        order = self.__dict__
        print( f"I would like a {order['size']}--inch pizza that is {order['style']} with {' and '.join(order['toppings'])}")


meat_lovers = Pizza()
meat_lovers.size = 16
meat_lovers.style = "Deep dish"
meat_lovers.add_topping("Pepperoni")
meat_lovers.add_topping("Olives")

meat_lovers.print_order()
'''I would like a 16--inch pizza that is Deep dish with Pepperoni and Olives'''

random_toppings = Pizza()
random_toppings.size = 16
random_toppings.style = "Thin Crust"
random_toppings.add_topping("Mushroom")
random_toppings.add_topping("Onion")
random_toppings.add_topping("Green Pepper")

random_toppings.print_order()
'''I would like a 16--inch pizza that is Thin Crust with Mushroom and Onion and Green Pepper'''
