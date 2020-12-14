class Ship:
    def __init__(self):
        self.x = 0  # east
        self.y = 0  # north
        self.direction = "E"

        self.operations = {
            "N": self.north,
            "S": self.south,
            "E": self.east,
            "W": self.west,
            "L": self.turn_left,
            "R": self.turn_right,
        }

    def parse_input(self):
        """
        Parses the input and performs the operations
        """
        with open("input_12.txt") as f:
            for line in f:
                operation = line[0]
                argument = int(line[1:])
                self.go(operation, argument)

    def go(self, operation, argument):
        """
        Performs the operation assigned to the given symbol. If that symbol
        is F, then it performs the operation assigned to the characters that
        marks the direction the ship is currently facing
        """
        if operation == "F":
            operation = self.direction

        self.operations[operation](argument)

    def north(self, argument):
        """
        Moves the ship north by the specified number of units
        """
        self.y += argument

    def south(self, argument):
        """
        Moves the ship south by the specified number of units
        """
        self.y -= argument

    def east(self, argument):
        """
        Moves the ship east by the specified number of units
        """
        self.x += argument

    def west(self, argument):
        """
        Moves the ship west by the specified number of units
        """
        self.x -= argument

    def turn_left(self, argument):
        """
        Rotates the ship counterclockwise the specified number of degrees
        """

        def _turn():
            """
            Rotates the ship counterclockwise 90 degrees
            """
            self.direction = {
                "N": "W",
                "W": "S",
                "S": "E",
                "E": "N",
            }[self.direction]

        for _ in range((argument // 90) % 4):
            _turn()

    def turn_right(self, argument):
        """
        Rotates the ship clockwise the specified number of degrees
        """

        def _turn():
            """
            Rotates the ship clockwise 90 degrees
            """
            self.direction = {
                "N": "E",
                "E": "S",
                "S": "W",
                "W": "N",
            }[self.direction]

        for _ in range((argument // 90) % 4):
            _turn()
