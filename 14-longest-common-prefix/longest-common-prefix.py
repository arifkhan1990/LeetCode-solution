class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()  # Sort if necessary, but it may not be needed for your specific case
        prefix = ""
        
        for group in zip(*strs):
            if len(set(group)) == 1:
                prefix += group[0]
            else:
                break

        return prefix
