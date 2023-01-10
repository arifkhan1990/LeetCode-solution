
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        good = Counter(s)
        good_val = sorted(good.values())
        return good_val[0] == good_val[len(good)-1]