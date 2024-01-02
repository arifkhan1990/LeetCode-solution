class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = set()
        for i in nums:
                pos = abs(i) - 1

                if nums[pos] < 0:
                    ans.add(abs(i))

                nums[pos] = -nums[pos]
        return ans