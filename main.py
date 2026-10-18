import random

IDENTIFIER = 1000
GRID_SIZE = 10

name = input("What is the name of the robot? ")

row, col = random.randrange(GRID_SIZE), random.randrange(GRID_SIZE)

DIRECTIONS = {"n": ("North", -1, 0),
              "e": ("East", 0, 1),
              "s": ("South", 1, 0),
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

def can_move(row, col, d_row, d_col):
    # True if one more step in this direction stays inside the grid
    return 0 <= row + d_row < GRID_SIZE and 0 <= col + d_col < GRID_SIZE

while can_move(row, col, d_row, d_col):
    print("Moving one step forward.")
    row = min(max(row + d_row, 0), GRID_SIZE - 1)
    col = min(max(col + d_col, 0), GRID_SIZE - 1)
    print(f"My current location is ({row}, {col}), facing {dir_name}")  

print("I have a wall in front of me!")  

keys = list(DIRECTIONS)
index = keys.index(direction)
direction = keys[(index + 1) % 4]
dir_name, d_row, d_col = DIRECTIONS[direction]
print(f"My current location is ({row}, {col}), facing {dir_name}")  
