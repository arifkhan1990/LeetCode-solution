class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        mod = 10**9 + 7
        dp = [0]*(high+1)
        dp[0] = 1
        for i in range(high):
            if i+zero <= high :
                dp[i+zero] += dp[i]
            if i+one <= high :
                dp[i+one] += dp[i]
        return sum(dp[low:high+1])%mod