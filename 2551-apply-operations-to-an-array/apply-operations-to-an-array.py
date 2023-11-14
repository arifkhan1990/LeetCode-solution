class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        ans = []
        sm = 0
        i = 0
        while i < len(nums):
            sm = 0
            if nums[i] == 0:
                i += 1
            else:
                if i < len(nums)-1 and nums[i] == nums[i+1]:
                    sm += nums[i] + nums[i+1]
                    i += 2
                else:
                    sm += nums[i]
                    i += 1
            
            if sm > 0:
                ans.append(sm)
        sc = len(nums) - len(ans)
        ans.extend([0]*sc)
        return ans