class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs)
        ans = strs[0]
        for i in range(1, len(strs)):
            for j in range(len(strs[i])):
                if j < len(ans) and ans[j] != strs[i][j]:
                    ans = strs[i][:j]
                    if ans == "":
                        return ""
        return ans
