
from collections import Counter


def min_difference(nums1, nums2):
    y = min(nums2)
    ans = float('inf')
    c2 = Counter(nums2)
    for x in nums1:
        a = [z + (y - x) for z in nums1]
        if Counter(a) >= c2:
            ans = min(ans, y - x)
    return ans
# Example 1
nums1 = [4,20,16,12,8] 
nums2 = [14,18,10]
print(min_difference(nums1, nums2))  # Output: -2

# Example 2
nums1 = [3,5,5,3]
nums2 = [7,7]
print(min_difference(nums1, nums2))  # Output: 2

nums1 = [5, 10, 15, 20, 25]  # After removing elements at indices [0, 4], nums1 becomes [10, 15, 20]
nums2 = [12, 17, 22] 
print(min_difference(nums1, nums2))  # Output: 2
