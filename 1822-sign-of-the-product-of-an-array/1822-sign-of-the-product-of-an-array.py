class Solution:
    def signFunc(self, x):
        if x > 0:
            return 1
        elif x < 0:
            return -1
        else:
            return 0
    def arraySign(self, nums: List[int]) -> int:
        sm = 1
        for i in nums:
            sm *= i
        return self.signFunc(sm)