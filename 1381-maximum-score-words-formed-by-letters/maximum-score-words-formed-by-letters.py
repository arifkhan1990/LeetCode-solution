class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        lcnt = Counter(letters)
        total_score = 0

        def solve(index, lcnt, cur_score):
            nonlocal total_score

            total_score = max(total_score, cur_score)
            if index == len(words):
                return

            for i in range(index, len(words)):
                tmp_cnt = copy.deepcopy(lcnt)
                word = words[i]
                word_score = 0
                isValid = True

                for ch in word:
                    if ch in tmp_cnt and tmp_cnt[ch] > 0:
                        tmp_cnt[ch] -= 1
                        word_score += score[ord(ch) - ord("a")]
                    else:
                        isValid = False
                        break
                if isValid:
                    solve(i + 1, tmp_cnt, cur_score + word_score)

        solve(0, lcnt, 0)
        return total_score