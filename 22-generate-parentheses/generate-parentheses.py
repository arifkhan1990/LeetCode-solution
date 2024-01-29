class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def solve(path="", char="(", open=0, close=0):
            if len(path) == n*2:
                ans.append(path)
            else:
                for ch in char:
                    cur_path = path+ch
                    if ch == '(':
                        c_open = open+1
                        c_close = close
                    else:
                        c_open = open
                        c_close = close + 1
                    new_ch = ""
                    if c_open < n:
                        new_ch += "("
                    if c_close < c_open:
                        new_ch += ")"
                    solve(cur_path, new_ch, c_open, c_close)
        solve()
        return ans