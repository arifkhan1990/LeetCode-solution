class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        ans, n = 1, len(nums)
        dp = [{} for _ in range(n)]
        for i in range(n):
            for j in range(i):
                d = nums[j] - nums[i]
                if d in dp[j]:
                    dp[i][d] = dp[j][d] + 1
                else:
                    dp[i][d] = 2
                ans = max(ans, dp[i][d])
        return ans
         