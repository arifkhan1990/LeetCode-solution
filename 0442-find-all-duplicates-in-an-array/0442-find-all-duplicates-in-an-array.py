class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        a = Counter(nums)
        ans = []
        for i in a:
            if a[i] > 1:
                ans.append(i)
        return ans