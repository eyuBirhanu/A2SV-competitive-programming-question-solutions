# Problem: Relative Ranks - https://leetcode.com/problems/relative-ranks/description/

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        scoreC = score[:]
        scoreC.sort(reverse=True)
        highest = {}

        for s in range(len(scoreC)):
            if s == 0:
                highest[scoreC[0]] = "Gold Medal"
            elif s == 1:
                highest[scoreC[1]] = "Silver Medal"
            elif s == 2:
                highest[scoreC[2]] = "Bronze Medal"
            else:
                highest[scoreC[s]] = f"{s+1}"


        for s in range(len(score)):
            score[s] = highest[score[s]]
        return score