class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        d = {')':'(', '}':'{', ']':'['}
        for i in s:
            if i in '({[':
                st.append(i)
            else:
                if len(st) != 0 and st[-1] == d[i]:
                    st.pop()
                else:
                    return False
        return True if len(st) == 0 else False