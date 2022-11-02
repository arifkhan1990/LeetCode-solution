class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        d = {}
        for i in items1:
            d[i[0]] = i[1]
        for i in items2:
            if i[0] in d:
                d[i[0]] += i[1]
            else:
                d[i[0]] = i[1]
        ans = []
        for i in d:
            temp = [i, d[i]]
            ans.append(temp)
        ans.sort()
        return ans