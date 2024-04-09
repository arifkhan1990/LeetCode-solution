class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        pro = [0]*(len(nums))
        n = len(nums)//2
        n1, n2 = nums[:-n], nums[-n:]
        
        for i in range(len(nums)):
            if i%2 == 0:
                pro[i] = n1[0]
                n1.pop(0)
        for i in range(1,len(nums)):
            if i%2 != 0:
                pro[i] = n2[0]
                n2.pop(0) 
        return pro