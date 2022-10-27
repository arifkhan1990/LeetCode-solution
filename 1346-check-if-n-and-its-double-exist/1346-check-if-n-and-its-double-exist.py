class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i in range(len(arr)):
            if arr[i] != 0 and arr[i]/2 in arr:
                return 1
            if arr[i] == 0 and 0 in arr[i+1:]:
                return 1
        return 0