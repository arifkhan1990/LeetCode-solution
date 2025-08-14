def count_right_triangles(grid):
    rows = len(grid)
    cols = len(grid[0])
    row_count = [0] * rows
    col_count = [0] * cols
    count = 0
    
    # Preprocess to count 1s in each row and column
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                row_count[i] += 1
                col_count[j] += 1
    
    # Iterate through each cell in the grid
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Calculate the count of right triangles using preprocessed information
                count += (row_count[i] - 1) * (col_count[j] - 1)
    
    return count

# Test cases
grid1 = [[0,1,0],[0,1,1],[0,1,0]]
grid2 = [[1,0,0,1],[0,1,0,1],[1,0,0,0]]
grid3 = [[1,0,1],[1,0,0],[1,0,0]]

print(count_right_triangles(grid1))  # Output: 2
print(count_right_triangles(grid2))  # Output: 0
print(count_right_triangles(grid3))  # Output: 2
