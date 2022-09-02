class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        ans = set()
        
        for i, n in enumerate(nums):
            if n in ans:
                return True
            ans.add(n)
        return False