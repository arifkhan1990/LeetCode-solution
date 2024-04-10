class Solution:
    def partitionString(self, s: str) -> int:
        ans = 1
        st = ""
        for i in s:
            if i in st:
                ans += 1
                st = i
            else:
                st += i
        return ans