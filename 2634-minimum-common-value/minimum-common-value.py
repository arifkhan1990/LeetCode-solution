class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        ans = set(nums1)
        for i in nums2:
            if i in ans:
                return i
        return -1