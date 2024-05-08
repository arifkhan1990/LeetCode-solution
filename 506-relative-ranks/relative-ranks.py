class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        index_dict = {score[i]: i for i in range(len(score))}
        sorted_scores = sorted(score, reverse=True)
        ranks = [None] * len(score)
        for i, s in enumerate(sorted_scores):
            if i == 0:
                ranks[index_dict[s]] = "Gold Medal"
            elif i == 1:
                ranks[index_dict[s]] = "Silver Medal"
            elif i == 2:
                ranks[index_dict[s]] = "Bronze Medal"
            else:
                ranks[index_dict[s]] = str(i + 1)
        return ranks