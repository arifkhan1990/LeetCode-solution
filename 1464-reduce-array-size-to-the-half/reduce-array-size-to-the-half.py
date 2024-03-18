class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        x = Counter(arr)
        sorted_counts = sorted(x.values(), reverse=True)
        ans = 0
        res = 0

        for i in sorted_counts:
            ans += i
            res += 1
            if ans >= (len(arr)//2):
                return res
        return res