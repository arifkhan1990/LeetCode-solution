class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        ans = nums[0]
        for i in range(1,len(nums)):
            ans = list(set(ans) & set(nums[i]))
        ans.sort()
        return ans