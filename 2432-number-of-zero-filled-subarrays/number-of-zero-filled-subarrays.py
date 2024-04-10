class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans = 0
        subArray = []
        i, j = 0, 0
        while i < len(nums):
            x = []
            while i < len(nums) and nums[i] == 0:
                x.append(nums[i])
                i += 1
            if len(x) > 0:
                subArray.append(x)
            else:
                i += 1
        
        for ar in subArray:
            n = len(ar)
            ans += n*(n+1)//2

        return ans

