class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        while l <= r :
            md = (l+r)//2

            if nums[md] == target:
                return md

            if nums[l] <= nums[md]:
                if nums[l] <= target < nums[md]:
                    r = md - 1
                else:
                    l = md + 1
            else:
                if nums[md] < target <= nums[r]:
                    l = md + 1
                else:
                    r = md - 1
        return -1
