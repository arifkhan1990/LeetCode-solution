class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        s, mx, l, r = 0, 0, 0, len(tokens)-1

        while l <= r:
            if power >= tokens[l]:
                power -= tokens[l]
                l += 1
                s += 1
                mx = max(mx, s)
            elif s > 0:
                power += tokens[r]
                r -= 1
                s -= 1
            else:
                break
        return mx