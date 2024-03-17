class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans  = []
        intervals.append(newInterval)
        sorted_data = sorted(intervals, key=lambda x: x[0])

        for i in range(len(sorted_data)):
            if len(ans) == 0:
                ans.append(sorted_data[i])
            else:
                if ans[-1][1] >= sorted_data[i][0]:
                    ans[-1][1] = max(ans[-1][1], sorted_data[i][1])
                else:
                    ans.append(sorted_data[i])
        return ans
