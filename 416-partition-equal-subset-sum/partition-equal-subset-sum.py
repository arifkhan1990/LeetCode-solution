class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        
        if total_sum%2:
            return 0
        
        target_sum = total_sum // 2
        dp = [0] * (target_sum + 1)
        dp[0] = 1
        
        for n in nums:
            for i in range(target_sum, n - 1, -1):
                dp[i] = dp[i] or dp[i-n]
                
        return dp[target_sum]