# Problem: Minimum Moves to Reach Target Score - https://leetcode.com/problems/minimum-moves-to-reach-target-score/

class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        moves = 0
        while target > 1:
            if maxDoubles < 1:
                break
            if target % 2 == 0 and maxDoubles > 0:
                target //= 2
                moves += 1
                maxDoubles -= 1
            else:
                target -= 1
                moves += 1
        
        moves += (target-1)
        return moves