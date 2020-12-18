import re
from math import prod


def parse_input():
    """
    Parses the input and returns a list of expressions
    """
    with open("input_18.txt") as f:
        return f.readlines()


def evaluate_1(expression):
    """
    Evaluates the equation according to rules in part 1
    """
    while "(" in expression:
        m = re.match(r"^(.*)\(([^()]*)\)(.*)$", expression)
        groups = m.groups()
        expression = f"{groups[0]}{evaluate_1(groups[1])}{groups[2]}"

    while "+" in expression or "*" in expression:
        m = re.match(r"^([0-9]+) ([+*]) ([0-9]+)(.*)$", expression)
        groups = m.groups()
        if groups[1] == "+":
            expression = f"{int(groups[0]) + int(groups[2])}{groups[3]}"
        else:
            expression = f"{int(groups[0]) * int(groups[2])}{groups[3]}"

    return expression


def evaluate_2(expression):
    """
    Evaluates the equation according to rules in part 2
    """
    while "(" in expression:
        m = re.match(r"^(.*)\(([^()]*)\)(.*)$", expression)
        groups = m.groups()
        expression = f"{groups[0]}{evaluate_2(groups[1])}{groups[2]}"

    return prod(
        sum(int(x) for x in chunk.split(" + ")) for chunk in expression.split(" * ")
    )


def get_total(evaluate, expressions):
    """
    Returns the total of all expressions evaluated using the given function
    """
    return sum(int(evaluate(expression)) for expression in expressions)


if __name__ == "__main__":
    expressions = parse_input()
    print(get_total(evaluate_1, expressions))
    print(get_total(evaluate_2, expressions))
