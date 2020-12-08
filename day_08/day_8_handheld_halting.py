from copy import deepcopy

from console import Console
from infinite_loop_error import InfiniteLoopError


def parse_input():
    """
    Parses the input and returns a list of instructions
    """
    with open("input_08.txt", "r") as f:
        instructions = [line.split() for line in f]

    return instructions


def part_1(instructions):
    """
    Finds the solution to part 1
    """
    console = Console(instructions)

    try:
        console.run()
    except InfiniteLoopError:
        return console.accumulator


def part_2(instructions):
    """
    Finds the solution to part 2
    """
    for i, instruction in enumerate(instructions):
        if instruction[0] == "acc":
            continue

        modified_instructions = deepcopy(instructions)
        if instruction[0] == "nop":
            modified_instructions[i][0] = "jmp"
        else:
            modified_instructions[i][0] = "nop"

        console = Console(modified_instructions)

        try:
            console.run()
            return console.accumulator
        except InfiniteLoopError:
            continue


if __name__ == "__main__":
    instructions = parse_input()
    print(f"Part 1: {part_1(instructions)}")
    print(f"Part 2: {part_2(instructions)}")
