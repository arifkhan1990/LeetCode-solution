class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c = Counter(nums)
        k = 0
        for i in range(3):
            for j in range(c[i]):
                nums[k] = i
                k += 1
        