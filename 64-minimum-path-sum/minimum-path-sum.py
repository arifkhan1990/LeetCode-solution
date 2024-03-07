class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        dp = [float('inf')]*(c+1)
        dp[1] = 0

        for r in grid:
            for i, num in enumerate(r):
                dp[i+1] = min(dp[i+1], dp[i]) + num

        return dp[-1]