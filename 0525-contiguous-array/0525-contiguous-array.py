class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        ans = 0
        maxL = 0
        res = {}
        for i in range(len(nums)):
            ans += -1 if nums[i] == 0 else 1
            if ans == 0:
                if maxL < i+1 :
                    maxL = i+1
            elif ans in res:
                maxL = max(maxL, i - res[ans])
            else:
                res[ans]= i
        return maxL