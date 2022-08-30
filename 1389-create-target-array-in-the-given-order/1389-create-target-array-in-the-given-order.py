class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        result = ['_'] * len(nums)
        dec = -1
        for i, n in enumerate(nums):
            if len(result) >= index[i]:
                for j in range (len(result)-1, index[i], dec):
                    result[j] = result[j-1]
            result[index[i]] = n
        return result