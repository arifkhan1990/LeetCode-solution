class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        rm = {}
        for i, n in  enumerate(nums2):
            rm[n] = i

        for i, n in  enumerate(nums1):
            mx = float("-inf")
            for j in range(rm[n], len(nums2)):
                if n < nums2[j]:
                    mx = nums2[j]
                    break
            if n < mx:
                nums1[i] = mx
            else:
                nums1[i] = -1
        return nums1