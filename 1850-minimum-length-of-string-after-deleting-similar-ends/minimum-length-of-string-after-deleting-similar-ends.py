class Solution:
    def minimumLength(self, s: str) -> int:
        while len(s) > 1:
            p = set()
            sp = set()
            i, j = 1, len(s) - 1
            while i < len(s):
                if s[i] == s[i-1]:
                    p.add(s[i-1])
                else:
                    p.add(s[i-1])
                    break
                i += 1
            
            while j > 0:
                if s[j] == s[j-1]:
                    sp.add(s[j])
                else:
                    sp.add(s[j])
                    break
                j -= 1
            if p != sp:
                break
            s = s[i:j]
            
        return len(s)