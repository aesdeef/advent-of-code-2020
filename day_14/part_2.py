def write_to_mem(target, number, mask, mem):
    """
    Writes the given value to all applicable memory addresses
    """
    target = f"{target:036b}"
    addresses = [""]
    for t, m in zip(target, mask):
        if m == "0":
            addresses = [address + t for address in addresses]
        elif m == "1":
            addresses = [address + "1" for address in addresses]
        else:
            addresses = [address + "0" for address in addresses] + [
                address + "1" for address in addresses
            ]

    for address in addresses:
        mem[int(address)] = number


def part_2():
    """
    Returns the solution for part 2
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
                write_to_mem(target, int(value), mask, mem)

    return sum(mem.values())
