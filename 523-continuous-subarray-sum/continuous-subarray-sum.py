class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        pre, prev, mp =0, 0, set()

        for i, n in enumerate(nums):
            pre += n
            pre %= k

            if pre in mp:
                return 1
            mp.add(prev)
            prev = pre
        return 0