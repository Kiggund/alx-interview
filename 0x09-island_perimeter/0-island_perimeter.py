#!/usr/bin/python3

def island_perimeter(grid):
    """
    Calculate the perimeter of an island in a grid.

    Args:
        grid (list of list of int): A 2D grid representing the map where 1 is land and 0 is water.

    Returns:
        int: The perimeter of the island.
    """
    rows, cols = len(grid), len(grid[0])
    perimeter = 0

    # Define the four possible directions: up, down, left, and right
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                # Count the exposed sides for this land cell
                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc
                    if (
                        new_row < 0
                        or new_row >= rows
                        or new_col < 0
                        or new_col >= cols
                        or grid[new_row][new_col] == 0
                    ):
                        perimeter += 1

    return perimeter
# Example usage
grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
print(island_perimeter(grid))  # Output: 12
