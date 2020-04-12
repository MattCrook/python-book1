import random

my_randoms = list()
for i in range(10):
    my_randoms.append(random.randrange(1, 6))

print(my_randoms)

"""
Print a message to the console indicating whether each value of
`number` is in the `my_randoms` list.
"""

numbers_1_to_10 = range(1, 11)

for number in numbers_1_to_10:
    the_numbers_match_ = False

    if number in my_randoms:
        the_numbers_match_ = True
        print(f'my_randoms list contains {number}')
    else:
        print(f'my_numbers list does not contain {number}')
