from cup import Cup


def parse_input(part=1):
    """
    Parses the input and returns a list of cup numbers
    """
    with open("input_23.txt") as f:
        return [int(x) for x in f.readline().strip()]


def turn_input_into_cups(input_):
    """
    Creates a Cup for each number in input_ and returns a dict of all cups
    """
    cups = {a: Cup(a) for a in input_}
    max_number = len(cups)

    for cup, next_cup in zip(input_, input_[1:] + input_[:1]):
        cups[cup].next = cups[next_cup]

    for i in range(2, max_number + 1):
        cups[i].one_below = cups[i - 1]
    cups[1].one_below = cups[max_number]

    return cups


def solve(cups, first_cup, turns):
    """
    Applies the specified actions to the cups a given number of times
    """
    current_cup = first_cup
    for _ in range(turns):
        next_three = [
            current_cup.next,
            current_cup.next.next,
            current_cup.next.next.next,
        ]

        destination_cup = current_cup.one_below
        while destination_cup in next_three:
            destination_cup = destination_cup.one_below

        current_cup.next = next_three[-1].next
        after_destination_cup = destination_cup.next
        destination_cup.next = next_three[0]
        next_three[-1].next = after_destination_cup

        current_cup = current_cup.next

    return cups


def part_1():
    """
    Returns the solution to part 1
    """
    input_ = parse_input()
    cups = turn_input_into_cups(input_)
    cups = solve(cups, first_cup=cups[input_[0]], turns=100)

    answer = []
    current_cup = cups[1].next
    while current_cup != cups[1]:
        answer.append(str(current_cup.number))
        current_cup = current_cup.next

    return "".join(answer)


def part_2():
    """
    Returns the solution to part 2
    """
    input_ = parse_input() + list(range(10, 1_000_001))
    cups = turn_input_into_cups(input_)
    cups = solve(cups, first_cup=cups[input_[0]], turns=10_000_000)

    return cups[1].next.number * cups[1].next.next.number


if __name__ == "__main__":
    print(part_1())
    print(part_2())
