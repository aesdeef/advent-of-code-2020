import re
from collections import Counter
from operator import xor


def check_letter_count(x, y, letter, password):
    """
    Returns true if the number of occurences of the letter in the password
    is within the given bounds
    """
    counter = Counter(password)
    min_count = int(x)
    max_count = int(y)
    return min_count <= counter[letter] <= max_count


def check_letter_position(x, y, letter, password):
    """
    Returns true if exactly one of the xth and yth characters of the password
    matches the given letter
    """
    x = int(x) - 1
    y = int(y) - 1
    return xor(password[x] == letter, password[y] == letter)


def count_valid_passwords(password_rule):
    """
    Counts the passwords that are valid according to the given rule
    """
    valid_password_count = 0

    match_rule = r"(\d+)-(\d+) ([a-zA-Z]): (.*)"
    with open("input_02.txt", "r") as f:
        for line in f:
            match = re.match(match_rule, line)
            if password_rule(*match.groups()):
                valid_password_count += 1

    return valid_password_count


if __name__ == "__main__":
    print(count_valid_passwords(check_letter_count))
    print(count_valid_passwords(check_letter_position))
