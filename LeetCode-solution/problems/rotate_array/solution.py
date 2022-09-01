class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        s , e = 0 , len(nums)-1
        k = k%(len(nums))
        while s < e:
            nums[s], nums[e] = nums[e], nums[s]
            s, e = s+1, e-1
        
        s,e = 0, k-1
        while s < e:
            nums[s], nums[e] = nums[e],nums[s]
            s, e = s+1, e-1
        
        s,e = k, len(nums)-1
        while s < e:
            nums[s], nums[e] = nums[e], nums[s]
            s,e = s+1, e-1