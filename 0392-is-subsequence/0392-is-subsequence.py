class Solution:
  def isSubsequence(self, s: str, t: str) -> bool:
        p = q = 0
        while p < len(s) and p <= q and q < len(t):
            if s[p] == t[q]:
                p , q = p+1, q+1
            else:
                q += 1
        return True if p == len(s) else False