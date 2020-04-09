class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s, t = [], []
        for x in S:
            if x == '#' and len(s) != 0:
                s.pop()
            elif(x != '#'):
                s.append(x)
        
        for x in T:
            if x == '#' and len(t) != 0:
                t.pop()
            elif(x != '#'):
                t.append(x)

        return True if s == t else False