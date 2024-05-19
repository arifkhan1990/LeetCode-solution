class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        ans = set()
        for i in range(len(nums)-1):
            if nums[i]%2 == nums[i+1]%2:
                return 0
        
        return 1