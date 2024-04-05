class Solution:
    def lengthLongestPath(self, input: str) -> int:
        def longestPath(s):
            data = s.split('\n')
            mx, curr = 0, {0: 0}

            for x in data:
                d = x.count('\t')
                x = x.replace('\t', '')

                if '.' in x:
                    mx = max(mx, curr[d] + len(x))
                else:
                    curr[d+1] = curr[d]  + len(x) + 1 
            return mx
        return longestPath(input)

