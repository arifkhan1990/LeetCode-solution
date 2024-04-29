class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        ans = 0
        for i in range(21):
            xor_v = 0

            for n in nums:
                bit_v = (1 << i) & n
                xor_v = xor_v ^ bit_v
            
            k_bit_v = (1 << i) & k
            if xor_v != k_bit_v:
                ans += 1
        return ans