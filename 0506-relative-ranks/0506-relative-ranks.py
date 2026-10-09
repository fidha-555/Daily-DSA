class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        sorted_score = sorted(score, reverse = True)
        result = []
        for i in score:
            rank = sorted_score.index(i)
            if rank == 0:
                result.append("Gold Medal")
            elif rank == 1:
                result.append("Silver Medal")
            elif rank == 2:
                result.append("Bronze Medal")
            else:
                result.append(str(rank+1))
        return result
    

        