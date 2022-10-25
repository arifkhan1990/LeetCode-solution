class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        i = 0
        ans = []
        while i < len(nums) and nums[i] <= target:
            if nums[i] == target:
                while i < len(nums) and nums[i] == target:
                    ans.append(i)
                    i += 1
            else:
                i += 1
        return ans