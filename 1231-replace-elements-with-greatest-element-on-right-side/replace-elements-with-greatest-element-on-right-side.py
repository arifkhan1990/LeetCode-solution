class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans = [0]*len(arr)
        mx = -1
        for i in range(len(arr)-1, -1, -1):
            ans[i] = mx
            mx = max(mx, arr[i])
        return ans