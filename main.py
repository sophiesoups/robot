identifier = 1000
grid_size = 10

name = input("What is the name of the robot? ")
row = int(input("What is its current row coordinate? "))
col = int(input("What is its current column coordinate? "))
direction = input("What is its initial direction [n|s|e|w]? ")
if direction == "n":
    dir = "North"
elif direction == "s":
    dir = "South"
elif direction == "e":
    dir = "East"
else:
    dir = "West"

row, col = [max(x, 0) for x in (row, col)]
row, col = [min(x, grid_size - 1) for x in (row, col)]

if row < (grid_size / 2) and col < (grid_size / 2):
    quadrant = "top left"
elif row < (grid_size / 2) and col >= (grid_size / 2):
    quadrant = "top right"
elif row >= (grid_size / 2) and col < (grid_size / 2):
    quadrant = "bottom left"
else:
    quadrant = "bottom right"

print(f"Hello, my name is {name} and my ID is {identifier}")
print(f"I am facing {dir}.")
print(f"My current location is ({row}, {col}). I am in the {quadrant} quadrant.")

