from collections import Counter
from functools import lru_cache


def parse_input():
    """
    Parses the input and returns the list of joltages including the charging
    outlet and the device's built-in adapter
    """
    with open("input_10.txt") as f:
        numbers = sorted(int(line) for line in f)

    return [0] + numbers + [numbers[-1] + 3]


def get_differences(numbers):
    """
    Returns the differences between each pair of consecutive numbers
    """
    return [numbers[i + 1] - numbers[i] for i in range(len(numbers) - 1)]


def part_1(differences):
    """
    Returns the answer to part 1
    """
    c = Counter(differences)
    return c[3] * c[1]


@lru_cache
def options(diffs):
    """
    Counts all the possible adapter arrangements given the jolt differences
    """
    if len(diffs) <= 2:
        return 1

    if diffs[0] + diffs[1] <= 3:
        return options(diffs[1:]) + options((diffs[0] + diffs[1],) + diffs[2:])
    else:
        return options(diffs[1:])


def part_2(differences):
    """
    Returns the answer to part 2
    """
    return options(tuple(differences))


if __name__ == "__main__":
    numbers = parse_input()
    differences = get_differences(numbers)
    print(part_1(differences))
    print(part_2(differences))
