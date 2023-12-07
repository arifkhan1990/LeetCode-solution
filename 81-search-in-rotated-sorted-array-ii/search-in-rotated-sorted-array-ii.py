class Solution:
    def binaryS(self, arr, l, r, t):
        while l <= r:
            m = (l+r)//2
            if arr[m] == t:
                return 1
            elif arr[m] > t:
                r = m -1
            else:
                l = m + 1
        return 0
    def search(self, nums: List[int], target: int) -> bool:
        k = -1
        for i in range(len(nums)-1,0,-1):
            if nums[i] < nums[i-1]:
                k = i-1
                break
        if self.binaryS(nums[:k+1], 0, k, target) or self.binaryS(nums[k+1:], 0, len(nums[k+1:])-1, target):
            return 1
        else:
            return 0