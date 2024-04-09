class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i, n in enumerate( set(nums) ):
            nums[i] = n
        for i in range(len(set(nums)), len(nums)):
            nums.pop()
        nums.sort()