def count_trees(grid, right, down):
    """
    Counts the trees given the grid and the slope
    """
    grid_height = len(grid)
    grid_width = len(grid[0])
    x, y = 0, 0
    tree_count = 0

    while y < grid_height:
        if grid[y][x % grid_width] == "#":
            tree_count += 1
        x += right
        y += down

    return tree_count


if __name__ == "__main__":
    with open("input_03.txt", "r") as f:
        grid = [line.strip() for line in f]

    slopes = (
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    )

    product = 1

    for slope in slopes:
        trees = count_trees(grid, *slope)
        product *= trees
        print(f"Right {slope[0]}, down {slope[1]}: {trees} trees")

    print(f"Product: {product}")
