from collections import Counter
from functools import lru_cache

with open("input_10.txt") as f:
    numbers = sorted(int(line) for line in f)

numbers = [0] + numbers + [numbers[-1] + 3]

differences = [numbers[i + 1] - numbers[i] for i in range(len(numbers) - 1)]

c = Counter(differences)

print(numbers)
print(differences)
print(c[1], c[3])
print(c[3] * c[1])

"""
it's enough to just look at the differences
the differences of 3 have to stay, but the chains of 1s can be reduced
"""

"""
11 - 11 2
111 - 111 21 12 3
1111 - 1111 211 121 112 22 31 13
11111 - 11111 2111 1211
111111 -
1111111 -
"""


@lru_cache
def options(diffs):
    if len(diffs) <= 2:
        return 1

    if diffs[0] + diffs[1] <= 3:
        return options(diffs[1:]) + options((diffs[0] + diffs[1],) + diffs[2:])
    else:
        return options(diffs[1:])


print(options(tuple(differences)))
