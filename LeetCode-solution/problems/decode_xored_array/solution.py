class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        ans = [first]
        for i in encoded:
            ans.append(first^i)
            first = first^i
        return ans