def solve(nums1, nums2):
    nums1.sort()
    nums2.sort()
    return nums2[0] - nums1[0]

print(solve([2,6,4],[9,7,5]))