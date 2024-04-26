class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n, res = len(grid), float('inf')
        dp = [[-1] * n for _ in range(n)]

        for j in range(n):
            dp[0][j] = grid[0][j]
        
        for i in range(1, n):
            for j in range(n):
                tmp = float('inf')
                for k in range(n):
                    if j != k:
                        tmp = min(tmp, grid[i][j] + dp[i-1][k])
                dp[i][j] = tmp
        
        for j in range(n):
            res = min(res, dp[n-1][j])
        
        return res