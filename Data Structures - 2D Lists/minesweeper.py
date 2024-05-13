"""
This code is used to solve the problem of transforming a grid of mines 
('#') and empty spaces ('-') into a grid where each empty space is 
replaced with a digit indicating the number of adjacent mines. 
    
"""

def count_adjacent_mines(grid):
    """
    Replace each dash '-' in the grid with a digit representing the 
    number of adjacent mines.
    
    Args:
        grid (list): A 2D grid of '#' and '-' characters, where '#' 
        represents a mine and '-' represents a mine-free spot.
        
    Returns:
        list: A 2D grid where each dash '-' is replaced by a digit 
        indicating the number of adjacent mines.
    """
    def is_valid_position(row, col):
        """Check if a given position is valid within the grid boundaries."""
        return 0 <= row < len(grid) and 0 <= col < len(grid[0])

    def count_adjacent(row, col):
        """Count the number of adjacent mines for a given position in the grid."""
        count = 0
        # Iterate over neighbouring cells
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:  # Skip the current cell
                    continue
                # Calculate coordinates of neighbouring cell
                new_row, new_col = row + i, col + j
                # Check if neighbouring cell contains a mine
                if is_valid_position(new_row, new_col) and grid[new_row][new_col] == '#':
                    count += 1
        return str(count)

    # Iterate over each cell in the grid
    for row_idx, row in enumerate(grid):
        for col_idx, cell in enumerate(row):
            # If the cell is a mine-free spot, count adjacent mines and replace the cell value
            if cell == '-':
                grid[row_idx][col_idx] = count_adjacent(row_idx, col_idx)
    
    return grid

# Example usage
grid = [
    ["-", "-", "-", "#", "#"],
    ["-", "#", "-", "-", "-"],
    ["-", "-", "#", "-", "-"],
    ["-", "#", "#", "-", "-"],
    ["-", "-", "-", "-", "-"]
]

# Get the grid with counts of adjacent mines
result = count_adjacent_mines(grid)

# Print the resulting grid
for row in result:
    print(row)