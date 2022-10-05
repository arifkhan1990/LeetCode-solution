class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        dis = [0]*26
        for i in range(len(s)-1):
            idx = s.find(s[i],i+1)
            if idx != -1:
                dis[ord(s[i]) - ord('a')] = idx -i -1
        for i in set(s):
            if dis[ord(i) - ord('a')] != distance[ord(i) - ord('a')]:
                return False
        return True