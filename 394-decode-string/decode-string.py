class Solution:
    def decodeString(self, s: str) -> str:
        st , curr_n , curr_s = [], 0, ''

        for ch in s:
            if ch.isdigit():
                curr_n = curr_n * 10 + int(ch)
            elif ch == '[':
                st.append((curr_s, curr_n))
                curr_s, curr_n = '', 0
            elif ch == ']':
                pre_s, num = st.pop()
                curr_s = pre_s + curr_s * num
            else:
                curr_s += ch
        return curr_s