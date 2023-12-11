class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        n = len(score)
        for i in range(n):
            max_index = i
            for j in range(i + 1, n):
                if score[j][k] > score[max_index][k]:
                    max_index = j
            score[i], score[max_index] = score[max_index], score[i]
        return score
        