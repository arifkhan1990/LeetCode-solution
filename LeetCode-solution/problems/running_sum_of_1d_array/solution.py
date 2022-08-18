class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ansList = []
        sum = 0
        for d in nums:
            sum += d
            ansList.append(sum)
        return ansList