from collections import deque
def shortest_special_subarray(nums, k):
    if k == 0:
        return 1
    min_length = float('inf')
    n = len(nums)
    arr = sorted(arr, reverse=True)
    
    for i in range(n):
        current_or = nums[i]
        if current_or >= k:
            return 1  
        for j in range(i + 1, n):
            current_or |= nums[j]
            if current_or >= k:
                min_length = min(min_length, j - i + 1)
                break  
    
    if min_length == float('inf'):
        return -1
    else:
        return min_length

# Test cases
print(shortest_special_subarray([1,2,3], 2))  # Output: 1
print(shortest_special_subarray([2,1,8], 10)) # Output: 3
print(shortest_special_subarray([1,2], 0))    # Output: 1
print(shortest_special_subarray([16,1,2,20,32], 45))  # Output: 5