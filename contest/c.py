def count_column_differences(matrix):
    count = 0
    rows = len(matrix)
    cols = len(matrix[0])
    
    for j in range(cols):  # Iterate through columns
        for i in range(rows - 1):  # Iterate through rows, except the last one
            if matrix[i][j] != matrix[i+1][j]:  # Check the difference between adjacent values
                count += 1
    
    return count

# Example usage:
matrix = [[4,2,2],[8,2,5],[1,5,2]]
grid = [[1, 1, 1],
        [0, 0, 0]]
grid1 = [[1],[2],[3]]
grid3 =  [[1,0,2],[1,0,2]]
print(count_column_differences(grid))  # Output will be 3
print(count_column_differences(grid1))  # Output will be 3
print(count_column_differences(grid3))  # Output will be 3
print(count_column_differences(matrix))  # Output will be 3
