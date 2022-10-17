class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        a = Counter(arr)
        ans = list(a.values())
        ans.sort()
        ans = ans[::-1]
        for i in range(len(ans)-1):
            if ans[i] <= ans[i+1]:
                return 0
        return 1