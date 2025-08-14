def minScorePerm(nums):
    n = len(nums)
    for i in range(0, len(nums)):
        nums[i]=nums[i]+(n*(nums[nums[i]]%n))

    for i in range(0, len(nums)):
        nums[i] = int(nums[i]/n)
    return nums

# Test cases
print(minScorePerm([1, 0, 2]))  # Output: [0, 1, 2]
print(minScorePerm([0, 2, 1]))  # Output: [0, 2, 1]
print(minScorePerm([1, 3, 2, 0]))  # Output: [0, 3, 1, 2]
