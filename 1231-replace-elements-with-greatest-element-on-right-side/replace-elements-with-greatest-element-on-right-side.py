class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans = []
        mx = -1
        for i in range(len(arr)-1, -1, -1):
            ans.append(mx)
            mx = max(mx, arr[i])
        return ans[::-1]