def is_valid_grid(grid):
    m = len(grid)
    n = len(grid[0])

    for i in range(m):
        for j in range(n):
            # Check if the cell below exists and if it's equal
            if i < m- 1 and grid[i][j] != grid[i + 1][j]:
                return False
            # Check if the cell to the right exists and if it's different
            if j < n-  1 and grid[i][j] == grid[i][j + 1]:
                return False


    return True

# Test cases
grid1 = [[1,0,2],[1,0,2]]
print(is_valid_grid(grid1))  # Output: True

grid2 = [[1,1,1],[0,0,0]]
print(is_valid_grid(grid2))  # Output: False

grid3 = [[1],[2],[3]]
print(is_valid_grid(grid3))  # Output: False
