# Using set() to create a set
languages = set()

# Using curly braces allows you to initialize the set with values
languages = {'english', 'mandarin chinese',
             'spanish', 'english', 'spanish', 'portugese'}
# Notice that both of those sets were constructed with some duplicate items. However, when you print out the set, the duplicates are gone.
print(languages)
{'english', 'mandarin chinese', 'portugese', 'spanish'}



# Create an empty set named showroom.
# Add four car model names to the set.
cars = set()
cars = {"bugatti", "ferrari", "audi", "ashton martin"}

# Print the length of your set.
print(len(cars))
# 4


# Pick one of the items in your show room and add it to the set.
# if you add the same car, or one that is already in there, it will not show up bc sets don't allow duplicates.
cars.add("camaro")
print(cars)
{'bugatti', 'camaro', 'audi', 'ferrari', 'ashton martin'}


# Using update(), add two more car models to your showroom with another set.
cars.update(("porche", "lexus"))
print(cars)
{'lexus', 'ferrari', 'porche', 'bugatti', 'camaro', 'audi', 'ashton martin'}


# You've sold one of your cars. Remove it from the set with the discard() method.
cars.discard("lexus")
print(cars)
{'ferrari', 'porche', 'bugatti', 'camaro', 'audi', 'ashton martin'}
