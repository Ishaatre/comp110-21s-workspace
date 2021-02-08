"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730393785"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
starting_line: str = "Your fortune cookie says..."

random_answer_1: str = "A beautiful, smart, and loving person will be coming into your life."

random_answer_2: str = "Your life will be happy and peaceful."

random_answer_3: str = "Soon life will be more interesting."

ending_line: str = "Now, go spread positive lines"

random_int: int = randint(1,3)

print(starting_line)

if random_int == 1: 
    print(random_answer_1)
else: 
    if random_int == 2: 
        print(random_answer_2)
    else: 
        print(random_answer_3)        
print(ending_line)