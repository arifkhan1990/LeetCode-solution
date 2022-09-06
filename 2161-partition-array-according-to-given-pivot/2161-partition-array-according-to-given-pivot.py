class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        s = []
        l = []
        m = []
        for n in nums:
            if n < pivot:
                s.append(n)
            elif n == pivot:
                m.append(n)
            else:
                l.append(n)
        
        for n in m:
            s.append(n)
        for n in l:
            s.append(n)
        return s