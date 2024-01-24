class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []

        subsets = []

        def dfs(i):
            if i >= len(nums):
                if subsets not in ans:
                    ans.append(subsets.copy())
                return
            subsets.append(nums[i])
            dfs(i+1)

            subsets.pop()
            dfs(i+1)
        dfs(0)
        return ans