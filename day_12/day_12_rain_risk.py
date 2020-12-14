from ship_part_1 import Ship as ShipPart1
from ship_part_2 import Ship as ShipPart2


def solve(Ship):
    """
    Solves the puzzle using the given ship class
    """
    ship = Ship()
    ship.parse_input()
    return abs(ship.x) + abs(ship.y)


if __name__ == "__main__":
    print(solve(ShipPart1))
    print(solve(ShipPart2))
