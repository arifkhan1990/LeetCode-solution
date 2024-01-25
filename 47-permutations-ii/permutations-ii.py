class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(start):
            if start == len(nums) - 1:
                ans.append(nums.copy())
                return
            used = set()

            for i in range(start, len(nums)):
                if nums[i] in used:
                    continue
                nums[start], nums[i] = nums[i], nums[start]

                backtrack(start+1)

                nums[start], nums[i] = nums[i], nums[start]

                used.add(nums[i])
        backtrack(0)
        return ans