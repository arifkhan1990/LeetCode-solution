class Solution:
    def magicalString(self, n: int) -> int:
        s = "122"
        ptr = 2
        l = '2'
        #12 2-11 1-2 1-1 2-22 1-1 221121122
        while len(s) < n:
            next_char = '2'* (int(s[ptr])) if l == '1' else '1'* (int(s[ptr]))
            s += next_char
            l = s[-1]

            ptr += 1
        ans = s[:n].count('1')
        return ans