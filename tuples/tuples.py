# tuple with animals

zoo = ("whale", "shark", "dolphin", "penguin", "lion",
       "tiger", "bear", "alligator", "ducks", "manatee")

# check to determine if animal is in the zoo
animal_to_find = "tiger"
if animal_to_find in zoo:
    print(f'{animal_to_find} was found in the zoo tuple.')

# find index of animal
print(zoo.index("manatee"))
# 9

(whale, shark, dolphin, penguin, lion, tiger, bear, alligator, ducks, manatee) = zoo

# or
# (first_animal, second_animal, third_animal, fourth_animal, fifth_animal, sixth_animal, seventh_animal, eighth_animal, ninth_animal, tenth_animal) = zoo
# print(seventh_animal) #'bear'

print(whale)  # 'whale'
print(ducks)  # 'ducks'

# convert tuple to list
zoo_list = list(zoo)
print(zoo_list)
# ['whale', 'shark', 'dolphin', 'penguin', 'lion', 'tiger', 'bear', 'alligator', 'ducks', 'manatee']

zoo_list.append("wolf")
zoo_list.append("elephant")
zoo_list.append("giraffe")

print(zoo_list)
# ['whale', 'shark', 'dolphin', 'penguin', 'lion', 'tiger', 'bear', 'alligator', 'ducks', 'manatee', 'wolf', 'elephant', 'giraffe']

# add multiple items to list with extend([])
zoo_list.extend(["hippo", "crocodile"])
print(zoo_list)

# convert back to tuple
# save off to new variable
new_zoo_tuple = tuple(zoo_list)
print(new_zoo_tuple)

# or reassign the zoo variable to a new tuple. Important to note that tuples are not mutable themselves, but you can do this
zoo = tuple(zoo_list)
print(zoo)
# ('whale', 'shark', 'dolphin', 'penguin', 'lion', 'tiger', 'bear', 'alligator', 'ducks', 'manatee', 'wolf', 'elephant', 'giraffe', 'hippo', 'crocodile')
