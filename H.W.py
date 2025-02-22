#Write a function named
#find2D that will take 2 parameters
#first parameter is a 2D list, 2nd parameter
#is the value we are searching for
#The function should return -1,-1 if the
#value is not found and it should return
#the position of the value in the list
#as a tuple if it's found
from random import *


grid = [[randint(10, 20) for _ in range(8)] for _ in range(8)]

# Print the grid
for row in grid:
    print(row)
