class Solution:
    def findMin(self, nums: List[int]) -> int:
        p = -1
        for i in range(len(nums)-1,-1,-1):
            if nums[i] < nums[i-1]:
                p = i-1
                break
        if len(nums) < 2:
            return nums[0]
        else:
            if p == 0:
                ans = min(nums[p], min(nums[p:]))
            else:
                ans = min(min(nums[:p]), min(nums[p:]))
            return ans