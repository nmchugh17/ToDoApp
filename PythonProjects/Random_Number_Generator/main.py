"""
This is a random number generator. We will enter a smaller and a larger whole number and then generate a random
number between the 2 whole numbers
"""

import random

lower_selected = False
value_error_message = "Incorrect input!\nPlease try again."
while not lower_selected:
    range_selected = False
    try:
        lower = int(input("Enter the lower bound:"))
        lower_selected = True
        while not range_selected:
            try:
                upper = int(input("Enter the upper bound:"))
                if upper > lower:
                    print(random.randrange(lower, upper, 1))
                    range_selected = True
                else:
                    print("Upper bound must be greater than the lower bound.\nPlease try again.")
            except ValueError:
                print(value_error_message)
                continue
    except ValueError:
        print(value_error_message)
        continue

