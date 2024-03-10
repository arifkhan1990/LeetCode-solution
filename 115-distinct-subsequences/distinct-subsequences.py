class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        def solve(i, j, dp):
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            if s[i] == t[j]:
                dp[i][j] = solve(i+1, j+1, dp) + solve(i+1, j, dp)
            else:
                dp[i][j] = solve(i+1,  j, dp)
            return dp[i][j]
        dp = [[-1]*(len(t)+1) for _ in range(len(s)+1)]
        return solve(0,0, dp)
            