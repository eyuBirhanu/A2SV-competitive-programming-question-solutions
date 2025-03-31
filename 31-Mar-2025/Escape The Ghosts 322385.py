# Problem: Escape The Ghosts - https://leetcode.com/problems/escape-the-ghosts/

import math
class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        my_step = abs(target[0]-0) + abs(target[1]-0)
        for i in range(len(ghosts)):
            ghosts[i] = abs(target[0]-ghosts[i][0]) + abs(target[1]-ghosts[i][1])
        for i in ghosts:
            if my_step >= i:
                return False
        return True

        