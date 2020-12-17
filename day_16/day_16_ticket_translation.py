import re
from math import prod


def parse_input():
    """
    Parses the input and returns a dict of rules and a list of tickets,
    starting with your ticket
    """
    rules = {}
    tickets = []

    with open("input_16.txt") as f:
        for line in f:
            rule_pattern = r"^([a-z ]+): ([0-9]+)-([0-9]+) or ([0-9]+)-([0-9]+)"
            match = re.match(rule_pattern, line)
            if match:
                name, *numbers = match.groups()
                numbers = [int(number) for number in numbers]
                rules[name] = ((numbers[0], numbers[1]), (numbers[2], numbers[3]))
            elif "," in line:
                tickets.append([int(number) for number in line.split(",")])

    return rules, tickets


def satisfies(number, rule):
    """
    Checks if the number satisfies the rule
    """
    for range_ in rule:
        min_, max_ = range_
        if min_ <= number <= max_:
            return True
    return False


def scan_ticket(rules, ticket):
    """
    Scans the ticket and returns whether the ticket is valid and the scanning
    error for that ticket
    """
    valid_ticket = True
    scanning_error = 0

    for number in ticket:
        valid_number = False

        for rule in rules.values():
            if satisfies(number, rule):
                valid_number = True
                break

        if not valid_number:
            valid_ticket = False
            scanning_error += number

    return valid_ticket, scanning_error


def scan_all_tickets(rules, tickets):
    """
    Scans all tickets and returns a list of valid tickets and the scanning
    error rate
    """
    valid_tickets = []
    scanning_error_rate = 0

    for ticket in tickets:
        is_valid, scanning_error = scan_ticket(rules, ticket)

        if is_valid:
            valid_tickets.append(ticket)
        else:
            scanning_error_rate += scanning_error

    return valid_tickets, scanning_error_rate


def deduce_field_order(rules, valid_tickets):
    """
    Deduces the order of the fields
    """
    possible_fields = []
    for numbers in zip(*valid_tickets):
        possibilities = set()
        for name, rule in rules.items():
            if all(satisfies(number, rule) for number in numbers):
                possibilities.add(name)
        possible_fields.append(possibilities)

    fixed = [False for options in possible_fields]

    while not all(fixed):
        newly_fixed = set()
        for i, options in enumerate(possible_fields):
            if not fixed[i] and len(options) == 1:
                newly_fixed |= options
                fixed[i] = True

        for i in range(len(possible_fields)):
            if not fixed[i]:
                possible_fields[i] -= newly_fixed

    return [options.pop() for options in possible_fields]


def part_2(fields, my_ticket):
    """
    Calculates the answer to Part 2
    """
    return prod(
        number
        for name, number in zip(fields, my_ticket)
        if name.startswith("departure")
    )


if __name__ == "__main__":
    rules, tickets = parse_input()
    my_ticket = tickets.pop(0)

    valid_tickets, scanning_error_rate = scan_all_tickets(rules, tickets)

    # The scanning error rate is the solution to Part 1
    print(scanning_error_rate)

    fields = deduce_field_order(rules, valid_tickets)

    print(part_2(fields, my_ticket))
