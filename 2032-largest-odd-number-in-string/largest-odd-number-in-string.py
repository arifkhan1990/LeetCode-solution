class Solution:
    def largestOddNumber(self, num: str) -> str:
        ans = ""
        for i in range(len(num)-1, -1, -1):
            if int(num[i])&1:
                ans = num[:i+1]
                break
        return ans