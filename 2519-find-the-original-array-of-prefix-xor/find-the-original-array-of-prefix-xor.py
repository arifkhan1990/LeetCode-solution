class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        n = len(pref)
        arr = [0] * n
        arr[0] = pref[0]
        for i in range(1, n):
            # Use XOR to combine the previous element with the current prefix
            arr[i] = pref[i-1] ^ pref[i]
        return arr
        