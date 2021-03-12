class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = res = 0
        for i in nums:
            if i == 0:
                res = max(ans, res)
                ans = 0
            else:
                ans += 1
        
        res = max(res, ans)
        return res
        