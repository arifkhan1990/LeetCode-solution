class Solution:
    def reverseString(self, s: List[str]) -> None:
        #  two pointer solution
        f , l = 0, len(s)-1
        while f <= l:
            s[f], s[l] = s[l], s[f]
            f , l = f+1, l-1
            
        # s[:] = s[::-1] python single line solution
        