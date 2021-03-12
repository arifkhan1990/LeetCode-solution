class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans = 0
        for x in nums:
            sn = str(x)
            if(len(sn)%2 == 0):
                ans += 1
            
        return ans