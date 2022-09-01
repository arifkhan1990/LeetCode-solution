class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low , high = 0, len(nums) - 1
        
        if target < nums[0]:
            return 0
        
        if target > nums[-1]:
            return len(nums)
        
        while low <= high:
            mid = (low+high)//2
            
            if nums[mid] == target:
                return mid
            elif nums[mid - 1] < target and nums[mid] > target:
                return mid
            elif nums[mid] > target:
                high = mid -1
            else:
                low = mid + 1