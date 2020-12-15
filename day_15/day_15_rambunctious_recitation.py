def parse_input():
    """
    Parses the input and returns a list of starting numbers
    """
    with open("input_15.txt") as f:
        return [int(x) for x in f.readline().split(",")]


def solve(starting_numbers, target_turn):
    """
    Finds the number spoken at the specified turn
    """
    occurences = {number: (i,) for i, number in enumerate(starting_numbers)}
    turn = len(starting_numbers)
    number = starting_numbers[-1]

    while turn < target_turn:
        if len(occurences[number]) == 1:
            number = 0
        else:
            number = occurences[number][-1] - occurences[number][-2]

        if number not in occurences:
            occurences[number] = (turn,)
        else:
            occurences[number] = (occurences[number] + (turn,))[-2:]

        turn += 1

    return number


if __name__ == "__main__":
    starting_numbers = parse_input()
    print(solve(starting_numbers, 2020))
    print(solve(starting_numbers, 30000000))
