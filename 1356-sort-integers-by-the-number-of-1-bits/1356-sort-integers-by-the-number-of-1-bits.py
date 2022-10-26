class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        a = dict()
        b = []
        arr.sort()
        for i in arr:
            if bin(i).count('1') in a:
                a[bin(i).count('1')].append(i)
            else:
                a[bin(i).count('1')] = []
                a[bin(i).count('1')].append(i)

        for i in sorted(a.keys()):
            b += a[i]
        return b