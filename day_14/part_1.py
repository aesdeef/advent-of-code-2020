def apply_mask(number, mask):
    """
    Applies the mask to the given value and returns the result
    """
    binary = f"{number:036b}"
    result_binary = "".join(
        masked if masked != "X" else digit for digit, masked in zip(binary, mask)
    )
    return int(result_binary, 2)


def part_1():
    """
    Returns the solution for part 1
    """
    with open("input_14.txt") as f:
        mask = ""
        mem = {}
        for line in f:
            target, value = line.split(" = ")
            if target == "mask":
                mask = value
            else:
                target = int(target.strip("mem[]"))
                mem[target] = apply_mask(int(value), mask)

    return sum(mem.values())
