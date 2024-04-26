class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        st = []
        for d in num:
            while k > 0 and st and st[-1] > d:
                st.pop()
                k -= 1
            st.append(d)
        
        while k > 0:
            st.pop()
            k -= 1
        
        while st and st[0] == '0':
            st.pop(0)
        
        return '0' if not st else ''.join(st)