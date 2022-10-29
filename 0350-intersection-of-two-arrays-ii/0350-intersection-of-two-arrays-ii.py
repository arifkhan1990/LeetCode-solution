class Solution:
    def binarySearch(self,nums, n):
        lo,hi = 0, len(nums)
        while lo <= hi:
            md = (lo + hi) >> 1

            if nums[md] == n:
                return nums[md]
            elif nums[md] < n:
                lo = md + 1
            else:
                hi = md - 1
        return -1
        
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        d = Counter(nums1)
        ans = []
        for i in nums2:
            if d[i] > 0:
                k = self.binarySearch(nums1,i)
                if k >= 0:
                    ans.append(k)
                d[i] -= 1
        return ans