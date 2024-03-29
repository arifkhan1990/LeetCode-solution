class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ans, n,i , j = 0, len(nums), 0 , 0
        mp = defaultdict(int)
        max_element = max(nums)
        
        while i < n:
            mp[nums[i]] += 1
            while mp[max_element] >= k:
                ans = ans + n - i
                mp[nums[j]] -= 1
                j += 1
            i += 1
        return ans