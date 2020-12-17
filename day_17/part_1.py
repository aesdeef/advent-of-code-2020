from functools import lru_cache


def parse_input():
    """
    Parses the input and returns a set of cubes
    """
    cubes = set()

    with open("input_17.txt") as f:
        for y, line in enumerate(f):
            for x, char in enumerate(line):
                if char == "#":
                    cubes.add((x, y, 0))

    return cubes


@lru_cache
def nearby(cube):
    """
    Returns a set of all cubes around the given cube
    """
    x, y, z = cube
    nearby_cubes = set()

    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            for dz in (-1, 0, 1):
                if any((dx, dy, dz)):
                    nearby_cubes.add((x + dx, y + dy, z + dz))

    return nearby_cubes


def iterate(cubes):
    """
    Performs one cycle on the given set of cubes and returns a new set of cubes
    """
    remaining = {cube for cube in cubes if len(nearby(cube) & cubes) in (2, 3)}

    potential_cubes = set.union(*(nearby(cube) for cube in cubes)) - cubes
    created = {cube for cube in potential_cubes if len(nearby(cube) & cubes) == 3}

    return remaining | created


def part_1():
    """
    Returns the solution for part 1
    """
    cubes = parse_input()

    for _ in range(6):
        cubes = iterate(cubes)

    return len(cubes)


if __name__ == "__main__":
    print(part_1())
