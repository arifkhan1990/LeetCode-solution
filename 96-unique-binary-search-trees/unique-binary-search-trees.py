class Solution:
    def numTrees(self, n: int) -> int:
        def solve(n, dp):
            if n <= 1:
                return 1
            
            if dp[n] != -1:
                return dp[n]

            ans = 0
            for i in range(1,n+1):
                ans += solve(i-1, dp) * solve(n-i, dp)
            dp[n] = ans
            return dp[n]

        dp = [-1]*(n+1)
        return solve(n, dp)