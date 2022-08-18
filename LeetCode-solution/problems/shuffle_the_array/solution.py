class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ansList = []
        for i in range(n):
            ansList.append(nums[i])
            ansList.append(nums[n+i])
        return ansList