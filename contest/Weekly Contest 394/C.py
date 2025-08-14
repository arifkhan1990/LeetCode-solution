def count_different_values_column_wise(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0]) if matrix else 0
    
    # Initialize a list to store counts of different values for each column
    column_counts = []
    
    # Iterate over each column
    for col in range(num_cols):
        # Initialize a set to store unique values in the current column
        unique_values = set()
        
        # Iterate over each row in the current column
        for row in range(num_rows):
            unique_values.add(matrix[row][col])
        
        # Count the number of unique values in the current column and append to the result list
        column_counts.append(len(unique_values))
    print(column_counts)
    ans = 0
    for i in range(len(column_counts)):
        ans += column_counts[i] - 1
    
    return ans

# # Test case
# grid = [[1, 1, 1],
#         [0, 0, 0]]

# print(minOperations(grid))  # Output will be 0, as all columns have the same value


# Test case
grid = [[1, 1, 1],
        [0, 0, 0]]
grid1 = [[1],[2],[3]]
grid3 = [[4,2,2],[8,2,5],[1,5,2]]
print(count_different_values_column_wise(grid))  # Output will be 3
print(count_different_values_column_wise(grid1))  # Output will be 3
print(count_different_values_column_wise(grid3))  # Output will be 3
