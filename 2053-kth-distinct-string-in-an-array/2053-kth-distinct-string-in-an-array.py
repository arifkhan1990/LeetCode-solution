class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        distinct =[]
        for i in range(len(arr)):
            if arr[i] not in arr[i+1:] and arr[i] not in arr[:i]:
                distinct.append(arr[i])
        return "" if k > len(distinct) else distinct[k-1]