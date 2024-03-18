class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[1])
        f, l = 1, points[0][1]
                                     
        for s, e in points:        
            if l < s:                    
                l = e                   
                f += 1                    
                                            
        return f 
