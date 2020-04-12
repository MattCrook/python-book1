my_family = {
    "sister": {
        "name": "Kaitlin",
        "age": 31
    },
    "mother": {
        "name": "Kim",
        "age": 60
    },
    "father": {
        "name": "Dave",
        "age": 60
    },
    "dog": {
        "name": "lucy",
        "age": 12
    }
}

# to convert an integer into a string in Python, it's str(integer_value)

for (key, value) in my_family.items():
  dict_variable = {key: value for (key, value) in my_family.items()}
  print(f'{value["name"]} is my {key} and they are {str(value["age"])} years old.')

# Output
  # Kaitlin is my sister and they are 31 years old.
  # Kim is my mother and they are 60 years old.
  # Dave is my father and they are 60 years old.
  # lucy is my dog and they are 12 years old.
