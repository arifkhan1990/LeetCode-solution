class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return 0
            
        newS = goal*2
        if newS.find(s) != -1:
            return 1
        else:
            return 0