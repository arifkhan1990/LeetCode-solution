class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[1])
        arrow, l = 1, points[0][1]
                                     
        for s, e in points:        
            if l < s:                    
                l = e                   
                arrow += 1                    
                                            
        return arrow 