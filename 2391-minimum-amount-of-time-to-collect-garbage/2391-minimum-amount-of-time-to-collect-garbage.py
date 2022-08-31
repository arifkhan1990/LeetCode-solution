class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        miniTime = 0
        hV = {'G': 0, 'P': 0, 'M': 0}
        for i, s in enumerate(garbage):
            sL = len(s)
            miniTime = miniTime + sL
            for c in s:
                hV[c] = i
        
        for i in  range(hV['G']):
            miniTime += travel[i]
            
        for i in  range(hV['P']):
            miniTime += travel[i]
            
        for i in  range(hV['M']):
            miniTime += travel[i]
        return miniTime