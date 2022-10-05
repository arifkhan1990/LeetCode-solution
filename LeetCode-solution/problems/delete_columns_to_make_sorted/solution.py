class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ar = []
        ans = 0
        for i in strs:
            ar.append(list(i))

        for i in range(len(ar[0])):
            x = [row[i] for row in ar]
            if x != sorted(x):
                ans += 1
        return ans