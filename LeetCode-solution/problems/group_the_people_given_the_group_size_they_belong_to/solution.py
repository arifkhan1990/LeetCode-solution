class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        ans = []
        for i in groupSizes:
            res = []
            for k,j in enumerate(groupSizes):
                if i == j:
                    if len(res) == j:
                        ans.append(res)
                        res = []
                    res.append(k)
                    groupSizes[k] = -1
            if i != -1 and len(res):
                ans.append(res)
                res = []
            
        return ans