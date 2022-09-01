# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low, high = 0, n-1
        
        while low <= high:
            mid = (low+high)//2
            if isBadVersion(mid) == False and isBadVersion(mid+1) == True:
                return mid+1
            elif isBadVersion(mid) == True:
                high = mid - 1
            elif isBadVersion(mid) == False:
                low = mid + 1