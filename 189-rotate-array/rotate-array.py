class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = k%len(nums)
        nums[n:],nums[:n] = nums[:-n], nums[-n:]