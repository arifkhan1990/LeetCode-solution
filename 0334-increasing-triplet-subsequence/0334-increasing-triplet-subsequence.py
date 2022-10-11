class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        ans = h = l = float('inf')
        for i in nums:
            if i <= h:
                h = i
            elif i <= l:
                l = i
            else:
                return 1
        return 0
            