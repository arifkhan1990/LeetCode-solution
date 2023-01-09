class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        mx = float('-inf')
        for i in strs:
            if i.isnumeric():
                mx = max(mx, int(i))
            else:
                mx = max(mx, len(i))
        return mx