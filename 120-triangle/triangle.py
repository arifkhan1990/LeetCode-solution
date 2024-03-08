class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = triangle[n - 1][:]

        for i in range(n - 2, -1, -1):
            for j in range(len(triangle[i])):
                dp[j] = min(dp[j] + triangle[i][j], dp[j + 1] + triangle[i][j])
        return dp[0]
