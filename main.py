import random

IDENTIFIER = 1000
GRID_SIZE = 10
dirs = ["n", "s", "e", "w"]

name = input("What is the name of the robot? ")

"""
row = int(input("What is its current row coordinate? "))
col = int(input("What is its current column coordinate? "))
direction = input("What is its initial direction [n|s|e|w]? ")
"""
row, col = random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)
direction = random.choice(dirs)

if direction == "n":
    dir = "North"
elif direction == "s":
    dir = "South"
elif direction == "e":
    dir = "East"
else:
    dir = "West"

"""
row, col = [max(x, 0) for x in (row, col)]
row, col = [min(x, GRID_SIZE - 1) for x in (row, col)]
"""

def determine_quadrant(row, col):
    if row < (GRID_SIZE / 2) and col < (GRID_SIZE / 2):
        quadrant = "top left"
    elif row < (GRID_SIZE / 2) and col >= (GRID_SIZE / 2):
        quadrant = "top right"
    elif row >= (GRID_SIZE / 2) and col < (GRID_SIZE / 2):
        quadrant = "bottom left"
    else:
        quadrant = "bottom right"
    return quadrant

print(f"Hello, my name is {name} and my ID is {IDENTIFIER}")
print(f"I am facing {dir}.")
print(f"My current location is ({row}, {col}). I am in the {determine_quadrant(row, col)} quadrant.")

if direction == "s" and row != (GRID_SIZE - 1):
    row += 1
elif direction == "n" and row != 0:
    row -= 1
elif direction == "e" and col != (GRID_SIZE - 1):
    col += 1
elif direction == "w" and col != 0:
    col -= 1

print("Moving one step forward.")
print(f"My current location is ({row}, {col}). I am in the {determine_quadrant(row, col)} quadrant.")  
