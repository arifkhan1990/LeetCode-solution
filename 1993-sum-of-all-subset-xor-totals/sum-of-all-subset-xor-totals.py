class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = 0

        for i in range(1 << n):
            sub_xor = 0
            for j in range(n):
                if i & (1 << j):
                    sub_xor ^= nums[j]
            total_sum += sub_xor
        return total_sum