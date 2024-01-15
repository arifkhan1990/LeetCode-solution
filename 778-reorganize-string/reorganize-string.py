from collections import Counter
class Solution:
    def reorganizeString(self, s: str) -> str:
        cnt = Counter(s)
        n = len(s)
        mx_data = cnt.most_common()[0]
        mx_ch, mx_v = mx_data[0], mx_data[1]

        if mx_v * 2 > n+1:
            return ""
        
        longest = []
        smallest = []
        longest.extend(mx_ch*mx_v)

        for k in cnt.keys():
            if k == mx_ch:
                continue
            
            for _ in range(cnt[k]):
                if (len(longest) + 1) * 2 <= n+1:
                    longest.append(k)
                else:
                    smallest.append(k)

        ans = ""
        for a, b in zip_longest(longest, smallest):
            ans += a
            if b is not None:
                ans += b
        
        return ans