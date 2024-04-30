class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        cnt = [0] * 1024
        cnt[0] = 1
        res, bitmask = 0, 0

        for ch in word:
            ch_idx = ord(ch) - ord('a')
            bitmask ^= 1 << ch_idx
            res += cnt[bitmask]
            for i in range(10):
                res += cnt[bitmask ^ (1 << i)]
            cnt[bitmask] += 1
        return res