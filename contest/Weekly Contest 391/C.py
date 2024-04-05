def count_alternating_subarrays(nums):
    count = 0
    length = 1 
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            length += 1
        else:
            count += (length * (length + 1)) // 2
            length = 1
    count += (length * (length + 1)) // 2  
    return count

# Example usage:
nums1 = [0, 1, 1, 1]
print(count_alternating_subarrays(nums1))  # Output: 5

nums2 = [1, 0, 1, 0]
print(count_alternating_subarrays(nums2))  # Output: 10

nums2 = [1, 0, 1, 0, 1]
print(count_alternating_subarrays(nums2))  # Output: 10
