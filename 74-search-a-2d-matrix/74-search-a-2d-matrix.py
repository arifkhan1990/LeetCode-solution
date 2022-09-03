class Solution:
    def binaryS(self, l, h, t, nums):
        
        while l <= h:
            m = (l+h)//2

            if nums[m] == t:
                return True
            elif nums[m] < t:
                l = m + 1
            else:
                h = m - 1
        return False
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if self.binaryS(0, len(matrix[0])-1, target, matrix[i]):
                return True
        return False
            