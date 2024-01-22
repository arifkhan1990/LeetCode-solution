class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        ar = {}
        mx = 0
        for i in grid:
            for j in i:
                mx = max(mx, j)
                if j in ar:
                    ar[j] += 1
                else:
                    ar[j] = 1
        
        duplicate, missing = 0, mx+1
        for i in range(1, mx+1):
            if i not in ar:
                missing = i
            else:
                if ar[i] > 1:
                    duplicate = i
        return [duplicate, missing]