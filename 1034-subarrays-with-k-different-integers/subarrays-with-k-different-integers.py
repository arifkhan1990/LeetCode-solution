class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def solve(nums, k):
            d = {}
            ans, cnt = 0, 0
            i, j = 0, 0
            n = len(nums)
            while i < n:
                if nums[i] not in d:
                    d[nums[i]] = 0
                d[nums[i]] += 1 
                while len(d) > k:
                    d[nums[j]] -= 1
                    if d[nums[j]] == 0:
                        del d[nums[j]]
                    j += 1
                ans += i - j + 1
                i += 1
            return ans
        return solve(nums, k) - solve(nums, k-1)
            