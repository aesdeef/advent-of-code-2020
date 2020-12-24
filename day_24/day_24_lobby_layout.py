from collections import Counter


def parse_input():
    """
    Parses the input and returns a list of directions for each tile
    """
    tiles = []

    with open("input_24.txt") as f:
        for line in f:
            tile = []
            line = (x for x in line.strip())
            for x in line:
                if x in "sn":
                    tile.append("".join((x, next(line))))
                else:
                    tile.append(x)
            tiles.append(tile)

    return tiles


def get_black_tiles(raw_tiles):
    """
    Turns the directions for each tile into a pair of coordinates and returns
    a set of the tiles left with the black side up
    """
    black_tiles = set()

    for tile in raw_tiles:
        c = Counter(tile)
        e = c["e"] - c["w"]
        ne = c["ne"] - c["sw"]
        se = c["se"] - c["nw"]

        tile_e = e * 2 + ne + se
        tile_n = ne - se
        tile = (tile_e, tile_n)

        if tile in black_tiles:
            black_tiles.remove(tile)
        else:
            black_tiles.add(tile)

    return black_tiles


def adjacent(tile):
    """
    Returns a set of tiles adjacent to the given tile
    """
    tile_e, tile_n = tile

    return {
        (tile_e + 2, tile_n),
        (tile_e - 2, tile_n),
        (tile_e + 1, tile_n + 1),
        (tile_e + 1, tile_n - 1),
        (tile_e - 1, tile_n + 1),
        (tile_e - 1, tile_n - 1),
    }


def flip_tiles(black_tiles, times=100):
    """
    Flips the tiles a given number of times according to the rules
    """
    for _ in range(times):
        remaining_tiles = {
            tile for tile in black_tiles if len(adjacent(tile) & black_tiles) in {1, 2}
        }

        possible_new_tiles = set()
        for tile in black_tiles:
            possible_new_tiles |= adjacent(tile)
        possible_new_tiles -= black_tiles

        new_tiles = {
            tile
            for tile in possible_new_tiles
            if len(adjacent(tile) & black_tiles) == 2
        }

        black_tiles = remaining_tiles | new_tiles

    return black_tiles


if __name__ == "__main__":
    raw_tiles = parse_input()
    black_tiles = get_black_tiles(raw_tiles)
    print(len(black_tiles))

    black_tiles = flip_tiles(black_tiles)
    print(len(black_tiles))
