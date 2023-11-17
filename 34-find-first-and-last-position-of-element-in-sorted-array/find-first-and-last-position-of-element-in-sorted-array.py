
def leftbinary(arr, l, r,t):
    ans = -1
    while l <= r:
        m = l + (r-l)//2
        if arr[m] == t:
            ans = m
            r = m - 1
        elif arr[m] < t:
            l = m + 1
        else:
            r = m - 1
    return ans

def rightbinary(arr, l, r,t):
    ans = -1
    while l <= r:
        m = l + (r-l)//2
        if arr[m] == t:
            ans = m
            l = m + 1
        elif arr[m] > t:
            r = m - 1
        else:
            l = m + 1
    return ans
        
class Solution:

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l,r = leftbinary(nums,0, len(nums)-1, target), rightbinary(nums,0, len(nums)-1, target)
        ans = [l,r]
        return ans