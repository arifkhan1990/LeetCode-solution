class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        x, y = len(nums1), len(nums2)
        l,h = 0, x

        while l <= h:
            pX = (l+h)//2
            pY = (x+y+1)//2 - pX

            mX1 = float("-inf") if pX == 0 else nums1[pX-1]
            mN1 = float("inf") if pX == x else nums1[pX]

            mX2 = float("-inf") if pY == 0 else nums2[pY-1]
            mN2 = float("inf") if pY == y else nums2[pY]

            if mX1 <= mN2 and mX2 <= mN1:
                if (x+y) % 2 == 0:
                    return (max(mX1,mX2) + min(mN1, mN2)) / 2
                else:
                    return max(mX1, mX2)
            elif mX1 > mN2:
                h = pX - 1
            else:
                l = pX + 1