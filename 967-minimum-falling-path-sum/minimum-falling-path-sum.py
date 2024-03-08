class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = matrix[0][:]
        
        for i in range(1, n):
            new_dp = [0] * n
            for j in range(n):
                if j == 0:
                    new_dp[j] = min(dp[j], dp[j+1]) + matrix[i][j]
                elif j == n-1:
                    new_dp[j] = min(dp[j], dp[j-1]) + matrix[i][j]
                else:
                    new_dp[j] = min(dp[j], dp[j-1], dp[j+1]) + matrix[i][j]
            dp = new_dp
        
        return min(dp)
