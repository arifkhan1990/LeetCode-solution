class Solution:
    def maxSum(self, nums, l, m, r):
        s = 0
        l_s = float('-inf')
        
        for i in range(m, l-1, -1):
            s += nums[i]
            l_s = max(l_s, s)
        
        s = 0
        r_s = float('-inf')
        
        for i in range(m, r+1):
            s += nums[i]
            r_s = max(r_s,s)
        return max(l_s+r_s - nums[m], l_s, r_s)
    
    def divideA(self, nums: List[int], l:int, r: int) -> int:
        if l > r:
            return float('-inf')
        if l == r:
            return nums[l]
        m = (l+r)//2
        return max(self.divideA(nums, l, m-1), self.divideA(nums, m+1, r), self.maxSum(nums, l, m, r))
    
    def maxSubArray(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        return self.divideA(nums, l, r)
        
        
        