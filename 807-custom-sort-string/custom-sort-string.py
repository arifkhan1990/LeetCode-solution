class Solution:
    def customSortString(self, order: str, s: str) -> str:
        def key(ch):
            return order.find(ch)
        
        ans = sorted(s, key=key)
        return "".join(ans)