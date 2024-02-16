class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        dp = [[0 for _ in range(c + 1)] for _ in range(r + 1)]

        def solve(dp, grid, r, c):
            if r == 0 and c == 0:
                return grid[r][c]
            if r < 0 or  c < 0:
                return float('inf')
            if dp[r][c] != 0: 
                return dp[r][c]
            dp[r][c] = grid[r][c] + min(solve(dp, grid, r - 1, c), solve(dp, grid, r, c - 1))
            return dp[r][c]
        
        return solve(dp, grid, r-1, c-1)