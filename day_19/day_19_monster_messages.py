import re
from functools import lru_cache

rules = {}
messages = set()

with open("input_19.txt") as f:
    for line in f:
        line = line.strip()
        if ":" in line:
            line = re.sub('"', "", line)
            name, rule = line.split(": ")
            rules[name] = set(rule.split(" | "))
        elif line:
            messages.add(line)


@lru_cache
def possibilities(rule_id):
    """
    Returns a set of all possibilities for the given rule
    """
    options = rules[rule_id]

    not_final = {option for option in options if re.search(r"\d", option)}
    final = options - not_final

    for option in not_final:
        parts = option.split()
        options = {""}
        for part in parts:
            if m := re.search(r"\d+", part):
                options = {a + b for a in options for b in possibilities(m.group())}
            else:
                options = {a + part for a in options}
        final |= options

    return final


def part_1():
    """
    Returns the solution to part 1
    """
    zeroes = possibilities("0")
    return len(messages & zeroes)


def part_2():
    """
    Returns the solution to part 2

    The function relies on the following observations:
    - the only rule that includes 8 and 11 is 0
    - the new rule 8 is equivalent to k repetitions of 42, where k is a positive
      integer
    - the new rule 11 is equivalent to k repetitions of 42 followed by k
      repetitions of 31, where k is a positive integer
    - hence the new rule 0 is equivalent to k repetitions of 42 followed by
      l repetitions of 31, where k and l are positive integers and k > l
    - the length of all possibilities for 42 is 8, and so is the length of all
      possibilities for 31
    """
    a = possibilities("42")
    b = possibilities("31")

    counter = 0
    for message in messages:
        b_count = 0
        while message[-8:] in b:
            b_count += 1
            message = message[:-8]

        if not b_count:
            continue

        a_count = 0
        while message[:8] in a:
            a_count += 1
            message = message[8:]

        if message:
            continue

        if a_count > b_count:
            counter += 1

    return counter


if __name__ == "__main__":
    print(part_1())
    print(part_2())
