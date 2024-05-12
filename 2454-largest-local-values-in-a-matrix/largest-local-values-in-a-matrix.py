class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        maxLocal = []
        
        # Iterate over the elements of grid, excluding the border elements
        for i in range(1, n - 1):
            row = []
            for j in range(1, n - 1):
                # Calculate the maximum value in the 3x3 submatrix centered at grid[i][j]
                max_val = max(
                    grid[i - 1][j - 1], grid[i - 1][j], grid[i - 1][j + 1],
                    grid[i][j - 1], grid[i][j], grid[i][j + 1],
                    grid[i + 1][j - 1], grid[i + 1][j], grid[i + 1][j + 1]
                )
                row.append(max_val)
            maxLocal.append(row)
        
        return maxLocal