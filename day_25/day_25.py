def parse_input():
    """
    Parses the input and returns a set of keys
    """
    with open("input_25.txt") as f:
        return {int(line) for line in f}


def get_encryption_key(public_keys):
    """
    Returns the encryption key
    """
    value = 1
    subject = 7
    loop_size = 0

    while True:
        loop_size += 1
        value = value * subject % 20201227

        if value in public_keys:
            public_keys.remove(value)
            other_key = public_keys.pop()

            return other_key ** loop_size % 20201227


if __name__ == "__main__":
    public_keys = parse_input()
    encryption_key = get_encryption_key(public_keys)
    print(encryption_key)
