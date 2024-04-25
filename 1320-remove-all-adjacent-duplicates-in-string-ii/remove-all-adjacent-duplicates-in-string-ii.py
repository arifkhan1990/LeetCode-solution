class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        st = []
        res = ""
        for i in range(len(s)):
            if st and st[-1][0] == s[i]:
                st[-1][1] += 1

                if st[-1][1] == k:
                    st.pop()
            else:
                st.append([s[i], 1])
        for ch, cnt in st:
            res += ch*cnt
        return res

