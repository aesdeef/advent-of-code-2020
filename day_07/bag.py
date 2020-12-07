from functools import cached_property


class Bag:
    # collection of all bag types with name as key
    collection = {}

    def __init__(self, rule):
        """
        Creates the bag type given the rule and adds it to the collection
        """
        container, containees = rule.split("contain")
        self.name = Bag.parse_phrase(container)
        self.containees = [
            Bag.parse_phrase(containee) for containee in containees.split(", ")
        ]

        if self.containees[0] == "no other":
            self.containees = []

        Bag.collection[self.name] = self

    @staticmethod
    def parse_phrase(phrase):
        """
        Parses the string to get the name of the bag type and the number, if present

        >>> parse_phrase('shiny gold bags')
        'shiny gold'
        >>> parse_phrase('3 shiny gold bags.')
        (3, 'shiny gold')
        """
        *number, adjective, colour, _ = phrase.split()
        if number:
            return (int(number[0]), f"{adjective} {colour}")
        return f"{adjective} {colour}"

    @cached_property
    def contains_shiny_gold(self):
        """
        Checks whether the bag contains a shiny gold bag
        """
        if not self.containees:
            return False

        if "shiny gold" in (name for _, name in self.containees):
            return True

        return any(
            Bag.collection[name].contains_shiny_gold for _, name in self.containees
        )

    @cached_property
    def inside_bag_count(self):
        """
        Counts the total number of bags contained in the bag
        """
        if not self.containees:
            return 0

        count = 0
        for number, name in self.containees:
            count += number * (1 + Bag.collection[name].inside_bag_count)

        return count
