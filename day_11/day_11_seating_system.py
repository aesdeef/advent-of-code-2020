from seat_part_1 import Seat as SeatPart1
from seat_part_2 import Seat as SeatPart2


def parse_input(Seat):
    """
    Parses the input and creates the seats using the provided class
    """
    with open("input_11.txt") as f:
        for y, line in enumerate(f):
            for x, seat in enumerate(line):
                if seat == "L":
                    Seat(x, y)


def solve(Seat):
    """
    Solves the puzzle using the provided seat class
    """
    parse_input(Seat)
    changed = True
    while changed:
        for seat in Seat.collection.values():
            seat.get_new_state()
        seat_changed = {seat.set_new_state() for seat in Seat.collection.values()}
        changed = True in seat_changed
    return len([seat for seat in Seat.collection.values() if seat.occupied])


if __name__ == "__main__":
    print(solve(SeatPart1))
    print(solve(SeatPart2))
