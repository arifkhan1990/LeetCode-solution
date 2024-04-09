class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        x = Counter(nums)
        i = 0

        for j in set(nums):
            if x[j] > 0:
                nums[i] = j
                i += 1
                x[j] -= 1

            if x[j] > 0:
                nums[i] = j
                i += 1
                x[j] -= 1
        for j in range(i, len(nums)):
            nums.pop()
        nums.sort()
        
