class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        ans = defaultdict(int)
        res , i, j = 0 , 0, 0

        while j < len(nums):
            ans[nums[j]] += 1

            while i <= j and ans[nums[j]] > k:
                ans[nums[i]] -= 1
                i += 1
            
            res = max(res, j -i + 1)
            j += 1
        return res