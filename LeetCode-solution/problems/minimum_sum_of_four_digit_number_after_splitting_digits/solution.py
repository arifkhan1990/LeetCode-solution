class Solution:
    def minimumSum(self, num: int) -> int:
        li = list(str(num))
        li.sort()
        n1 = int(li[0])*10 + int(li[3])
        n2 = int(li[1])*10 + int(li[2])
        return n1+n2