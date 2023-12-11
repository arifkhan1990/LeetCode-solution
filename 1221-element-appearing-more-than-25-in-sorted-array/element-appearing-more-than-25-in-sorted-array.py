class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        f = {}
        ans = 0
        for i in arr:
            if i not in f:
                f[i] = 1
            else:
                f[i] += 1
            
            if f[i] > int(n*0.25):
                ans = i
        return ans
        