class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        for i in strs:
            x = tuple(sorted(i))
            if x in hash_map:
                hash_map[x].append(i)
            else:
                hash_map[x] = [i]
        return hash_map.values()
