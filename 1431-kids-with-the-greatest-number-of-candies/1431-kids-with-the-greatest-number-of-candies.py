class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxC = max(candies)
        ans = []
        for i in candies:
            if maxC <= i+extraCandies:
                ans.append(True)
            else:
                ans.append(False)
        return ans