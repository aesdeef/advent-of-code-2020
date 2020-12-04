from itertools import combinations

# get all the numbers from the input
with open("input_01.txt", "r") as f:
    numbers = {int(x) for x in f.readlines()}

# find the pair of numbers that sums up to 2020 and return the product
for x, y in combinations(numbers, 2):
    if x + y == 2020:
        print(x * y)

# find the three of numbers that sums up to 2020 and return the product
for x, y, z in combinations(numbers, 3):
    if x + y + z == 2020:
        print(x * y * z)
