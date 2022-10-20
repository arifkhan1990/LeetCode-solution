class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ansS = []
        sm = 0
        for i in nums:
            sm += i
            ansS.append(sm)
            if sm < 0:
                sm = 0
        return max(ansS)