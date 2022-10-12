class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        if nums != []:
            s = str(nums[0])
            for i in range(1,len(nums)):
                if nums[i] - nums[i-1] != 1:
                    if s != str(nums[i-1]):
                        ans.append(s+"->"+str(nums[i-1]))
                    else:
                        ans.append(s)
                    s = str(nums[i])

            if len(nums) > 1 and nums[-1] - nums[-2] == 1:
                ans.append(s+"->"+str(nums[-1]))
            else:
                ans.append(s)
        return ans
            