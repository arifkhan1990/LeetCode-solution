class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l = 0
        sm = sum(nums[:k])
        ans = sm/k
        for i in range(k,len(nums)):
            sm -= nums[l]
            sm += nums[i]
            mx = sm/k
            if ans < mx:
                ans = mx
            l += 1
        return ans
