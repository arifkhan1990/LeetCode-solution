class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        l, r = 0, len(nums)-1

        pro = [0]*(len(nums))
        
        for i in range(len(nums)):
            if i%2 == 0:
                pro[i] = nums[l]
                l += 1
            else:
                pro[i] = nums[r]
                r -= 1
        return pro