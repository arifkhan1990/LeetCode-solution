class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mainArr = []
        for i in nums1:
            mainArr.append(i)
        for i in nums2:
            mainArr.append(i)
        mainArr.sort(reverse=False)
        
        ln = len(mainArr)//2

        if len(mainArr)%2:
            return mainArr[ln]
        else:
            return (mainArr[ln - 1] + mainArr[ln])/2.0
        