class Solution:
    def trap(self, A: List[int]) -> int:
        n = len(A)
        l, r = 0, n-1
        ans = 0
        lmx , rmx = float('-inf'), float('-inf')
        
        while l < r:
            lmx = max(lmx, A[l])
            rmx = max(rmx, A[r])
            if lmx < rmx:
                ans += lmx - A[l]
                l += 1

            else:
                ans += rmx - A[r]
                r -= 1
                
        return ans