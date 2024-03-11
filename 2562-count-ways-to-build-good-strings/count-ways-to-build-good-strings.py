class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = [0]*(high+1)
        dp[0] = 1
        mod = 1000000007
        for i in range(1,high+1):
            if i>=zero:
                dp[i] = dp[i-zero]
            if i >= one:
                dp[i] = (dp[i]+dp[i-one])%mod
        
        return sum((dp[low:high+1]))%mod