class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        def solve(op1, sign, op2):
            if sign == '+':
                return op1 + op2
            elif sign == '*':
                return op1 * op2
            elif sign == '-':
                return op2 - op1
            else:
                return int(op2 / op1)
        for i in tokens:
            if i not in "+-*/":
                st.append(int(i))
            else:
                st.append(solve(st.pop(), i, st.pop()))
        return st[0]