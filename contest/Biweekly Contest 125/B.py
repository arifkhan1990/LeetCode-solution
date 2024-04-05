import heapq

def min_operations(nums, k):
    operations = 0
    heapq.heapify(nums)
    
    while nums[0] < k:
        x = heapq.heappop(nums)
        y = heapq.heappop(nums)  # corrected line
        heapq.heappush(nums, min(x, y) * 2 + max(x, y))
        operations += 1
        
    return operations

# Example usage:
nums = [1, 2, 3]
k = 4
print(min_operations(nums, k))  # Output: 1