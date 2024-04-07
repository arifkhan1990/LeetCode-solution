class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if k == 0:
            sm = [sum(abs(n)) for n in nums]
            if sm == 0:
                return 1
        
        mp = {0: -1}
        prefixSum = 0
        for i, n in enumerate(nums):
            prefixSum += n
            if prefixSum%k in mp:
                if i - mp[prefixSum%k] > 1:
                    return 1
            else:
                mp[prefixSum%k] = i
        return 0