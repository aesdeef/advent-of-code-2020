def parse_input():
    """
    Parses the input and returns a list of groups of sets of answers
    """
    groups = []

    with open("input_06.txt", "r") as f:
        current_group = []

        for line in f:
            if answers := set(line.strip()):
                current_group.append(answers)
            else:
                groups.append(current_group)
                current_group = []
        groups.append(current_group)

    return groups


def count_answers_anyone(groups):
    """
    Counts the number of answers given by at least one member of the group
    and returns the sum of those counts
    """
    return sum(len(set.union(*group)) for group in groups)


def count_answers_everyone(groups):
    """
    Counts the number of answers given by all members of the group
    and returns the sum of those counts
    """
    return sum(len(set.intersection(*group)) for group in groups)


if __name__ == "__main__":
    groups = parse_input()
    print(count_answers_anyone(groups))
    print(count_answers_everyone(groups))
