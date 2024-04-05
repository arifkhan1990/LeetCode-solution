def min_operations(nums, k):
    count = 0
    for num in nums:
        if num < k:
            count += 1
    return count

# Example usage:
nums = [2,11,10,1,3]
k = 10
print(min_operations(nums, k))  # Output: 3