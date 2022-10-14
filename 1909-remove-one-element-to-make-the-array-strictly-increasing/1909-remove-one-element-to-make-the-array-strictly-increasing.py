class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        tmp = []
        ar = []
        for i in nums:
            if len(ar) < 1:
                ar.append(i)
            elif i <= ar[-1]:
                if len(tmp) < 1:
                    tmp.append(i)
                else:
                    if i >= tmp[-1]:
                        x = ar.pop()
                        y = tmp.pop()
                        ar.append(y)
                        tmp.append(x)
                        ar.append(i)
                    else:
                        ar.append(i)
            else:
                ar.append(i)
        br = ar.copy()
        br.sort()

        for i in range(len(br)-1):
            if br[i] == br[i+1]:
                return 0
        return 1 if ar == br else 0