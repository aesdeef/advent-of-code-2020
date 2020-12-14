class Ship:
    def __init__(self):
        self.waypoint_x = 10  # east
        self.waypoint_y = 1  # north
        self.x = 0
        self.y = 0
        self.direction = "E"

        self.operations = {
            "N": self.north,
            "S": self.south,
            "E": self.east,
            "W": self.west,
            "L": self.turn_left,
            "R": self.turn_right,
            "F": self.forward,
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
        Performs the operation assingned to the given symbol
        """
        self.operations[operation](argument)

    def north(self, argument):
        """
        Moves the waypoint north by the specified number of units
        """
        self.waypoint_y += argument

    def south(self, argument):
        """
        Moves the waypoint south by the specified number of units
        """
        self.waypoint_y -= argument

    def east(self, argument):
        """
        Moves the waypoint east by the specified number of units
        """
        self.waypoint_x += argument

    def west(self, argument):
        """
        Moves the waypoint west by the specified number of units
        """
        self.waypoint_x -= argument

    def turn_left(self, argument):
        """
        Rotates the waypoint around the ship counterclockwise the given number
        of degrees
        """

        def _turn():
            """
            Rotates the waypoint around the ship counterclockwise 90 degrees
            """
            self.waypoint_x, self.waypoint_y = -self.waypoint_y, self.waypoint_x

        for _ in range((argument // 90) % 4):
            _turn()

    def turn_right(self, argument):
        """
        Rotates the waypoint around the ship clockwise the given number of
        degrees
        """

        def _turn():
            """
            Rotates the waypoint around the ship clockwise 90 degrees
            """
            self.waypoint_x, self.waypoint_y = self.waypoint_y, -self.waypoint_x

        for _ in range((argument // 90) % 4):
            _turn()

    def forward(self, argument):
        """
        Moves the ship forward to the waypoint a number of times equal to
        the given value
        """
        self.x += argument * self.waypoint_x
        self.y += argument * self.waypoint_y
