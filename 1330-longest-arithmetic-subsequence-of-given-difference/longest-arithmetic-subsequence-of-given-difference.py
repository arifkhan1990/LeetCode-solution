class Solution:
    def longestSubsequence(self, arr: List[int], diff: int) -> int:
        dp = {}
        for i in arr:
            sm = 1
            if i - diff in dp:
                sm += dp[i-diff]
            dp[i] = sm
        return max(dp.values())