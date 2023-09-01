class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for w in strs:
            ar = []
            p = ''.join(sorted(w))
            
            if p in ans:
                ans[p].append(w)
            else:
                ans[p] = [w]

        return ans.values()
