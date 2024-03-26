class Solution:
    def splitArray(self, arr: List[int], k: int) -> int:
        l = max(arr)
        h = sum(arr)
        ans = l

        def split_cnt(arr, m):
            s, c = 0, 1
            for i in range(len(arr)):
                if s+arr[i] > m:
                    c += 1
                    s = arr[i]
                else:
                    s += arr[i]
            return c

        while l <= h:
            m = (l+h)//2
            n = split_cnt(arr, m)
            if n > k:
                l = m + 1
            else:
                ans = m
                h = m - 1
        return ans