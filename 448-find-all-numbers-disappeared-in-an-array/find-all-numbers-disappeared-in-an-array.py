class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        for x in nums:
            idx = abs(x) - 1
            nums[idx] = -abs(nums[idx])

        for i in range(0, len(nums)):
            if nums[i] > 0:
                ans.append(i+1)
        return ans