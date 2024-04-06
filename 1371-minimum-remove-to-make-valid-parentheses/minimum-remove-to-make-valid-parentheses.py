class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        st = []
        parentheses = []
        ans = []
        for i, x in enumerate(s):
            if x == '(':
                st.append((x, i))
            elif st and x == ')':
                if st[-1][0] == '(':
                    parentheses.append((st[-1][0], st[-1][1]))
                    parentheses.append((x, i))
                    st.pop()
            if x not in "()":
                ans.append(x)
            else:
                ans.append(" ")

        for i, d in enumerate(parentheses):
            ans[d[1]] = d[0]
        ans = " ".join(ans)
        return "".join(ans.split())