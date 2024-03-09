class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        ans = {}
        res = 0
        for i in nums1:
            if i not in ans:
                ans[i] = 1
        
        for i in nums2:
            if i in ans:
                return i
        return -1