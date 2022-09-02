class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashD = {}
        
        for i, n in enumerate(nums):
            if target - n in hashD:
                return [hashD[target-n], i]
            hashD[n] = i
        return []