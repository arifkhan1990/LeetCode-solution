class Solution:
    def decodeString(self, s: str) -> str:
        stc, cn , cst = [], 0 , ''

        for ch in s:
            if ch.isdigit():
                cn = cn * 10 + int(ch)
            elif ch == '[':
                stc.append((cst, cn))
                cst, cn = '', 0
            elif ch == ']':
                pst, n = stc.pop()
                cst = pst + cst * n
            else:
                cst += ch
        return cst
