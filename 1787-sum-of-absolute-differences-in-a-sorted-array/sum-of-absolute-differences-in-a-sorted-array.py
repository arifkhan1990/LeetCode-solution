class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # Calculate prefix and suffix sums
        prefix_sum, suffix_sum = 0, sum(nums)
        
        for i in range(n):
            # Update prefix and suffix sums for the next iteration
            prefix_sum += nums[i]
            # Update result for the current element
            nums[i] = (((i+1) * nums[i] - prefix_sum) + (suffix_sum - prefix_sum) - (n - i - 1)*nums[i])

        return nums       