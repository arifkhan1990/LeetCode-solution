class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        ans = []
        left, right = 0, len(nums) - 1
        while left <= right:
            ans.append((nums[left] + nums[right]) / 2)
            left += 1
            right -= 1
        return min(ans)