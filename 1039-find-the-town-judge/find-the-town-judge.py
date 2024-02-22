class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        a,b= [0]*(n+1), [0]*(n+1)
        for x in trust:
            a[x[0]] += 1
            b[x[1]] += 1
        
        for i in range(1,n+1):
            if b[i] == n-1 and a[i] == 0:
                return i
        return -1