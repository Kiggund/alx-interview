#!/usr/bin/python3

def island_perimeter(grid):
    rows, cols = len(grid), len(grid[0])
    perimeter = 0

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    # Iterate through the grid
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Count exposed sides for this land cell
                exposed_sides = 4
                if is_valid(i - 1, j) and grid[i - 1][j] == 1:
                    exposed_sides -= 1  # Top neighbor
                if is_valid(i + 1, j) and grid[i + 1][j] == 1:
                    exposed_sides -= 1  # Bottom neighbor
                if is_valid(i, j - 1) and grid[i][j - 1] == 1:
                    exposed_sides -= 1  # Left neighbor
                if is_valid(i, j + 1) and grid[i][j + 1] == 1:
                    exposed_sides -= 1  # Right neighbor
                
                perimeter += exposed_sides

    return perimeter

# Example usage:
grid_example = [
    [0, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 0, 0]
]

print(island_perimeter(grid_example))
