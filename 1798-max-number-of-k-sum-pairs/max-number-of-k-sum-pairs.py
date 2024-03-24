from collections import Counter
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        ans, i, j = 0, 0, len(nums)-1
        nums.sort()

        while i < j:
            if nums[i]+nums[j] == k:
                ans += 1
                i += 1
                j -= 1
            elif nums[i] + nums[j] < k:
                i += 1
            else:
                j -= 1
        return ans
