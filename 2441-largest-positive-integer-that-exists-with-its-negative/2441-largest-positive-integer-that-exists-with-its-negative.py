class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        nums = nums[::-1]
        ans = 0

        for i in range(len(nums)):
            if nums[i] > 0:
                if -nums[i] in nums:
                    ans = nums[i]
                    break
        return ans if ans != 0 else -1
        