class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        
        dp = [1] * n
        counts = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[i] < dp[j] + 1:
                        dp[i] = dp[j] + 1
                        counts[i] = counts[j]
                    elif dp[i] == dp[j] + 1:
                        counts[i] += counts[j]

        max_length = max(dp)
        result = 0
        for i in range(n):
            if dp[i] == max_length:
                result += counts[i]
        return result