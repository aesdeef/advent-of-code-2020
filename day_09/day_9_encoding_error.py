def parse_input():
    """
    Parses the input and returns a list of numbers
    """
    with open("input_09.txt") as f:
        return [int(line) for line in f]


def find_first_invalid_number(numbers, n=25):
    """
    Finds the first invalid number on the list, where n is the length of
    the preamble
    """
    seen = numbers[:n]
    for number in numbers[n:]:
        valid = False
        choices = seen[-n:]

        for choice in choices:
            matching_number = number - choice
            if matching_number in choices and choice != matching_number:
                valid = True
                seen.append(number)
                break

        if not valid:
            return number


def find_encryption_weakness(numbers, invalid_number):
    """
    Finds the encryption weakness given the list of numbers
    and the first invalid number
    """
    for i, number in enumerate(numbers):
        chain = [number]

        for next_number in numbers[i + 1 :]:
            chain.append(next_number)
            chain_sum = sum(chain)

            if chain_sum == invalid_number:
                return min(chain) + max(chain)

            if chain_sum > invalid_number:
                break


if __name__ == "__main__":
    numbers = parse_input()
    invalid_number = find_first_invalid_number(numbers)
    print(invalid_number)
    print(find_encryption_weakness(numbers, invalid_number))
