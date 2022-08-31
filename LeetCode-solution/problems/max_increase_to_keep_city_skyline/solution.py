class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        maxIncrease = sum([sum(i) for i in grid])
        rotedArr = list(zip(*grid))

        for i in grid:
            for j in rotedArr:
                maxIncrease -= min(max(i), max(j))
        
        return maxIncrease*-1