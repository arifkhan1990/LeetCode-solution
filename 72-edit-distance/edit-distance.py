class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @cache
        def solve(w1, w2, i, j) :
            if i == len(w1):
                return len(w2) - j
            if j == len(w2):
                return len(w1) - i
            
            ans = 0
            if w1[i] == w2[j]:
                return solve(w1,w2, i+1, j+1)
            else:
                insert = 1 + solve(w1,w2, i, j+1)
                delete = 1 + solve(w1,w2, i+1, j)
                replace = 1 + solve(w1,w2, i+1, j+1)
                ans = min([insert, delete, replace])
            return ans
        return solve(word1, word2, 0, 0)
