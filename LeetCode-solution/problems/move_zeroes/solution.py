class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zI = nonzI = 0
        
        while nonzI < len(nums):
            if nums[nonzI] != 0:
                nums[zI], nums[nonzI] = nums[nonzI], nums[zI]
                zI += 1
            nonzI += 1
        
        