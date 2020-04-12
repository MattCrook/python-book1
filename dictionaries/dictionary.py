# Create an empty dictionary
animal = dict()
# Add k/v pairs
animal["name"] = "Kevin"
animal["breed"] = "Bulldog"
animal["age"] = 5

# Create the dictionary with k/v pairs and assign to variable
animal = {
    "name": "Kevin",
    "breed": "Bulldog",
    "age": 5
}

for (key, value) in animal.items():
    print(f"{key}: {value}")

# Output
# name: Kevin
# breed: Bulldog
# age: 5


"""
Create a dictionary with key value pairs to
represent words (key) and its definition (value)
"""

"""
Add several more words and their definitions
   Example: word_definitions["Awesome"] = "The feeling of students when they are learning Python"
"""

"""
Use square bracket lookup to get the definition of two
words and output them to the console with `print()`
"""

"""
Loop over the dictionary to get the following output:
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
"""

word_definitions = dict()

word_definitions["dictionary"] = "dictionary"
word_definitions["list"] = "array"
word_definitions["tuple"] = "array-immutable"
word_definitions["set"] = "array-no-duplicates"

word_definitions = {
    "dictionary": "object",
    "list": "array",
    "tuple": "array-immutable",
    "set": "array-no-duplicates"
}

print(word_definitions["dictionary"])
# output: object


for (key, value) in word_definitions.items():
    print(f'The definition of {key} is {value}.')

# Output:
  # The definition of dictionary is object.
  # The definition of list is array.
  # The definition of tuple is array-immutable.
  # The definition of set is array-no-duplicates.


# Write a for loop to turn the k,v pairs into sentences

idioms = {
    "Penny": ["A", "penny", "for", "your", "thoughts"],
    "Injury": ["Add", "insult", "to", "injury"],
    "Moon": ["Once", "in", "a", "blue", "moon"],
    "Grape": ["I", "heard", "it", "through", "the", "grapevine"],
    "Murder": ["Kill", "two", "birds", "with", "one", "stone"],
    "Limbs": ["It", "costs", "an", "arm", "and", "a", "leg"],
    "Grain": ["Take", "what", "someone", "says", "with", "a", "grain", "of", "salt"],
    "Fences": ["I'm", "on", "the", "fence", "about", "it"],
    "Sheep": ["Pulled", "the", "wool", "over", "his", "eyes"],
    "Lucifer": ["Speak", "of", "the", "devil"],
}

for (key, value) in idioms.items():
        space = " "
        print(f'{key}: {space.join(value)}')

#Output
  # Penny: A penny for your thoughts
  # etc...
