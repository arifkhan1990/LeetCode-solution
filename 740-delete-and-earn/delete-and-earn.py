class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        n = len(nums)
        sm = [0]*(10001)

        for i in set(nums):
            sm[i] = nums.count(i) * i
        
        dp = [0] * (10001)
        dp[1] = sm[1]
        
        for i in range(2,10001):
            dp[i] = max(dp[i-2] + sm[i], dp[i-1])
        
        return dp[10000]