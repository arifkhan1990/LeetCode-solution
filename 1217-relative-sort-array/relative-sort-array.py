class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        x = Counter(arr1)
        ans = []
        for i in arr2:
            for j in range(x[i]):
                ans.append(i)
            del x[i]
        for key in sorted(x.keys()):
            ans.extend([key] * x[key])
        return ans