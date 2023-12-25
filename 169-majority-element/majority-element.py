class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt, n, ans = 0, len(nums), 0
        fre = {}
        for i in nums:
            if i in fre:
                fre[i] += 1
            else:
                fre[i] = 1
            
            if cnt < fre[i]:
                cnt = fre[i]
                ans = i
        return ans
