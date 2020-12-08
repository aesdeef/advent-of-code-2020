from infinite_loop_error import InfiniteLoopError


class Console:
    def __init__(self, instructions):
        self.accumulator = 0
        self.pointer = 0
        self.instructions = instructions
        self.history = []

        self.operations = {
            "acc": self.acc,
            "jmp": self.jmp,
            "nop": self.nop,
        }

    def run(self):
        """
        Keeps running the instruction until the last one in the list is executed
        """
        keep_running = True
        last_instruction_pointer = len(self.instructions) - 1

        while keep_running:
            if self.pointer == last_instruction_pointer:
                keep_running = False

            if self.pointer in self.history:
                raise InfiniteLoopError

            self.history.append(self.pointer)
            self.execute(self.instructions[self.pointer])

    def execute(self, instruction):
        """
        Delegates the execution of the instruction to the appropriate method
        """
        operation, *parameters = instruction
        self.operations[operation](*parameters)

    def acc(self, arg):
        """
        Executes the acc operation
        """
        self.accumulator += int(arg)
        self.pointer += 1

    def jmp(self, arg):
        """
        Executes the jmp operation
        """
        self.pointer += int(arg)

    def nop(self, *args):
        """
        Executes the nop operation
        """
        self.pointer += 1
