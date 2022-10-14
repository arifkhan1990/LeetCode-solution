class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return 0
        mx = max(arr)
        Lf = arr.index(mx)
        if Lf == len(arr)-1 or Lf == 0:
            return 0
        for i in range(1,Lf+1):
            if arr[i] <= arr[i-1]:
                return 0
        for i in range(Lf, len(arr)-1):
            if arr[i] <= arr[i+1]:
                return 0
        return 1