def code_to_number(code):
    """
    Convert part of the seat code to row/column number
    """
    binary = "".join("1" if character in {"B", "R"} else "0" for character in code)
    return int(binary, 2)


def get_coordinates(code):
    """
    Convert the seat code to row and column numbers
    """
    return (
        code_to_number(code[:7]),
        code_to_number(code[7:]),
    )


def get_seat_id(row, column):
    """
    Get the seat ID
    """
    return row * 8 + column


def load_input():
    """
    Load all the seat codes from the input and convert them to seat coordinates
    """
    with open("input_05.txt", "r") as f:
        seats = {get_coordinates(line.strip()) for line in f}
    return seats


def find_empty_seat(seat_ids):
    """
    Find the missing seat id
    """
    for i in range(min(seat_ids) + 1, max(seat_ids) - 1):
        if i not in seat_ids and i - 1 in seat_ids and i + 1 in seat_ids:
            return i


if __name__ == "__main__":
    seats = load_input()
    seat_ids = {get_seat_id(*seat) for seat in seats}
    print(f"Highest seat id: {max(seat_ids)}")
    print(f"Your seat: {find_empty_seat(seat_ids)}")
