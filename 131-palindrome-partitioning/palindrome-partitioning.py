class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans =  []
        
        def solve(s, subString):
            if len(s) == 0:
                ans.append(subString[:])
                return
            
            for i in range(1, len(s)+1):
                x = s[:i]
               
                if x == x[::-1]:
                    subString.append(x)
                    y = s[i:]
                    solve(y, subString)
                    subString.pop()
        solve(s, [])
        return ans