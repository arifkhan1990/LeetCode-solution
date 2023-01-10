class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        totalS = sum(nums)
        
        leftPrefixS = 0
        
        for  i , n in enumerate(nums):
            if leftPrefixS == totalS - leftPrefixS - n:
                return i
            leftPrefixS += n
        return -1
        