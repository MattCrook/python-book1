# Same function in JS turned to Python

# const createPerson = (firstName, lastName, age, occupation) = > {
#     return {
#         firstName,
#         lastName,
#         age,
#         occupation
#     }
# }

# melissa = createPerson("Melissa", "Bell", 25, "Software Developer")

# Function and variable names are snake case instead of camel case


def create_person(first_name, last_name, age, occupation):
    return {
        "first_name": first_name,
        "last_name": last_name,
        "age": age,
        "occupation": occupation,
    }


melissa = create_person("Melissa", "Bell", 25, "Software Developer")

# the * indicates there could be varying number of arguments


def add(*list_of_numbers):
    sum = 0

    for number in list_of_numbers:
        sum = sum + number

    print("Sum:", sum)


add(3, 5)
add(4, 5, 6, 7)
add(1, 2, 3, 5, 6)

# ** is a kwarg means there is a keyword associated with the argument.


def list_person(**person):
    for key, value in person.items():
        print(f"{key} is {value}")


melissa = list_person(first_name="Melissa", last_name="Bell",
                      age=25, occupation="Software Developer")

# ************************************************* #

# basically FIZZBUZZ in python
for num in range(1, 100):
  if num % 5 == 0 and num % 7 == 0:
        print("chickenMonkey")
  elif num % 7 == 0:
        print("monkey")
  elif num % 5 == 0:
        print("chicken")
  else:
      print(num)

# Written as a function
def chicken_monkey(numbers):
    for num in numbers:
      if num % 5 == 0 and num % 7 == 0:
        print("chickenMonkey")
      elif num % 7 == 0:
        print("monkey")
      elif num % 5 == 0:
        print("chicken")
      else:
        print("chickenShit")

chicken_monkey(range(1, 100))
# **************************************** #
