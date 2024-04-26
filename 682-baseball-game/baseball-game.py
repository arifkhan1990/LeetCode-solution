class Solution:
    def calPoints(self, operations: List[str]) -> int:
        st = []
        ans = 0
        for i in operations:
            if i == 'C':
                ans -= st.pop()
            elif i == 'D':
                st.append(st[-1]*2)
                ans += st[-1]
            elif i == '+':
                sm = sum(st[-2:])
                st.append(sm)
                ans += sm
            else:
                st.append(int(i))
                ans += st[-1]

        return ans