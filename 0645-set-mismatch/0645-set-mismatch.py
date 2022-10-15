class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        a = Counter(nums)
        Fsm = sum(nums)
        Csm = (len(nums) * (len(nums)+1))//2
        tp = a.most_common(1)
        return [tp[0][0], Csm - (Fsm - tp[0][0])]

