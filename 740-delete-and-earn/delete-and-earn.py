class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        n = len(nums)
        mx = max(nums)+1
        sm = [0]*(mx)

        for i in set(nums):
            sm[i] = nums.count(i) * i
        
        dp = [0] * (mx)
        dp[1] = sm[1]
        
        for i in range(2,mx):
            dp[i] = max(dp[i-2] + sm[i], dp[i-1])
        
        return dp[mx-1]