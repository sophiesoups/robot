import random

IDENTIFIER = 1000
GRID_SIZE = 10

name = input("What is the name of the robot? ")

row, col = random.randrange(GRID_SIZE), random.randrange(GRID_SIZE)

DIRECTIONS = {"n": ("North", -1, 0),
              "s": ("South", 1, 0),
              "e": ("East", 0, 1),
              "w": ("West", 0, -1)}

direction = random.choice(list(DIRECTIONS))
dir_name, d_row, d_col = DIRECTIONS[direction]

def determine_quadrant(row, col):
    half = GRID_SIZE / 2
    vertical = "top" if row < half else "bottom"
    horizontal = "left" if col < half else "right"
    return f"{vertical} {horizontal}"

def print_location(row, col):
    return f"I am in the {determine_quadrant(row, col)} quadrant"

print(f"Hello, my name is {name} and my ID is {IDENTIFIER}")
print(f"I am facing {dir_name}.")
print(f"My current location is ({row}, {col}). {print_location(row, col)}")

if direction == "s" and row != (GRID_SIZE - 1):
    row += 1
elif direction == "n" and row != 0:
    row -= 1
elif direction == "e" and col != (GRID_SIZE - 1):
    col += 1
elif direction == "w" and col != 0:
    col -= 1

print("Moving one step forward.")
print(f"My current location is ({row}, {col}). {print_location(row, col)}")  
