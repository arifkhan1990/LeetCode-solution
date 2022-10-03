import operator

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        ans = list(zip(names,heights))
        ans = sorted(ans, key = lambda ans: ans[1])
        ans.reverse()
        ans = list(list(zip(*ans))[0])
        return ans
        