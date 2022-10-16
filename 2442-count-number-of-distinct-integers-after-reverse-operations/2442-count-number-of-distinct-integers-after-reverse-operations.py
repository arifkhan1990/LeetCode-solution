class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        ans = set(nums)
        for i in nums:
            m = str(i)
            ans.add(int(m[::-1]))
        return len(ans)
            