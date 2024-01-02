class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        fps, curr = 0,0
        fp = [0]*n

        for i , x in enumerate(nums):
            if fp[i]:
                curr ^= 1
            
            if x^curr == 0:
                fps += 1
                curr ^= 1

                if i + k > n:
                    return -1
                if i + k < n:
                    fp[i+k] = 1
        return fps