class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            s = target - nums[i]
            if s in nums[i+1:]:
                k = nums[i+1:].index(s)
                return [i, i+1+k]