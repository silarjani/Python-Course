#All the code does is randomly set the food variable to either 'apple','grape', 'bacon', 'steak', 'worm', or 'dirt'.
#When you run the prewritten code, food will be randomly assigned.  You task is to write code that will classify what food is.
# a) If food is set to either 'apple' or 'grape', your code should print 'fruit'.
# b) If food is set to either 'bacon' or 'steak', your code should print 'meat'
# c) If food is set to either 'dirt' or 'worm' your code should print 'yuck'

# NO TOUCHING ======================================
from random import choice

food = choice(['apple', 'grape', 'bacon', 'steak', 'worm'])
# NO TOUCHING ======================================


# YOUR CODE GOES HERE
if food == 'apple' or food == 'grape':
    print("fruit")
elif food == 'bacon' or food == 'steak':
    print("meat")
else:
    print("yuck")