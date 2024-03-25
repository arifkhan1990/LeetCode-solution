class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        x = Counter(nums)
        return [i for i , j in x.items() if j > 1]