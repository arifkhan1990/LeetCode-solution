class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums = [n*n for n in nums]
        s, e = 0, len(nums)-1
        ans = []
        while s <= e:
            if nums[s] < nums[e]:
                ans.append(nums[e])
                e -= 1
            else:
                ans.append(nums[s])
                s += 1
        ans.reverse()
        return ans