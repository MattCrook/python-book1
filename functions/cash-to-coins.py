'''
Create a function that will take all your coins and convert it to the cash amount.
'''
# The function should look at each key (pennies, nickels, dimes and quarters) and perform the appropriate math
# on the integer value to determine how much money you have in dollars. Store that value in a variable named `dollarAmount` and print it.
import math

def calc_dollars(**coins):
    dollarAmount = 0
    dollarAmount += (coins["pennies"] * .01) + (coins["nickels"]
                                                * .05) + (coins["dimes"] * .10) + (coins["quarters"] * .25)
    print(f'${dollarAmount}')


calc_dollars(pennies=342, nickels=9, dimes=32, quarters=4)
# $8.07

# Now do the reverse. Convert the dollar amount into the coins that make up that dollar amount.

dollarAmount = 8.69


def coins_to_dollar_amount(cash):
    piggyBank = {
        "pennies": 0,
        "nickels": 0,
        "dimes": 0,
        "quarters": 0
    }
    cents = cash * 100
    # used math floor to round decimal down...

    piggyBank["quarters"] = math.floor(cents // 25)  # dividing 869 by 25 = 34.76 === 34 quarters
    cents -= piggyBank["quarters"] * 25  # must subtract that value to get new cents value >>> 869 - 34 then * 25 = 850 === 19 left

    piggyBank["dimes"] = math.floor(cents // 10)
    cents -= piggyBank["dimes"] * 10

    piggyBank["nickels"] = math.floor(cents // 5)
    cents -= piggyBank["nickels"] * 5

    piggyBank["pennies"] = math.floor(cents)
    print("piggybank:", piggyBank)

coins_to_dollar_amount(8.69)
piggybank: {'pennies': 4, 'nickels': 1, 'dimes': 1, 'quarters': 34}
