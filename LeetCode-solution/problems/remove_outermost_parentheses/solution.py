class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        
        ans = []
        b = 0
        
        for c in S:
            if b:
                ans.append(c)
            
            b += 1 if c == '(' else -1

            if not b:
                ans.pop()
                
        return "".join(ans)