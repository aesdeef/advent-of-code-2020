from functools import cached_property


class Seat:
    collection = {}

    def __init__(self, x, y):
        """
        Initialises the seat and adds it to the collection
        """
        self.x = x
        self.y = y
        self.occupied = False
        self.occupied_new = False
        Seat.collection[(self.x, self.y)] = self

    @cached_property
    def adjacent(self):
        """
        Finds all seats that are next to this seat
        """
        seats = set()
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                if not (dx == 0 and dy == 0):
                    seat_x = self.x + dx
                    seat_y = self.y + dy
                    if (seat_x, seat_y) in Seat.collection.keys():
                        seats.add(Seat.collection[(seat_x, seat_y)])
        return seats

    def get_new_state(self):
        """
        Determines whether the seat should be occupied in the next iteration
        """
        if not self.occupied and not any(seat.occupied for seat in self.adjacent):
            self.occupied_new = True
        elif (
            self.occupied
            and len({seat for seat in self.adjacent if seat.occupied}) >= 4
        ):
            self.occupied_new = False

    def set_new_state(self):
        """
        Sets the new value of occupied and returns True if it's different
        from the current one, otherwise returns False
        """
        if self.occupied != self.occupied_new:
            self.occupied = self.occupied_new
            return True
        return False
