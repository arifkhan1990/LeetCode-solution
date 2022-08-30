class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ansString = ['']*len(indices)
        
        for i, n in enumerate(indices):
            ansString[n] = s[i]
        return ''.join(ansString)