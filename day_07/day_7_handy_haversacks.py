from bag import Bag


def parse_input():
    """
    Parses the input and creates bag types for each rule
    """
    with open("input_07.txt", "r") as f:
        for line in f:
            Bag(line)


if __name__ == "__main__":
    contain_shiny_gold = {
        bag for bag in Bag.collection.values() if bag.contains_shiny_gold
    }
    print(f"{len(contain_shiny_gold)} type(s) of bag contain a shiny gold bag")

    shiny_gold = Bag.collection["shiny gold"]
    print(f"A shiny gold bag contains {shiny_gold.inside_bag_count} bag(s)")
