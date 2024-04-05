class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        ans = []
        d = ""
        l = 0
        for i in s[::-1]:
            if i != '-':
                l += 1
                d += i.upper()
            if l == k:
                ans.append(d[::-1])
                l = 0
                d = ""
        if d != "":
            ans.append(d[::-1])
        return "-".join(ans[::-1])