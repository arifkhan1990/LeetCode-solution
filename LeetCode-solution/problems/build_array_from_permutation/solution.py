class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ansList = []
        for i, d in enumerate(nums):
            ansList.append(nums[nums[i]])
        return ansList