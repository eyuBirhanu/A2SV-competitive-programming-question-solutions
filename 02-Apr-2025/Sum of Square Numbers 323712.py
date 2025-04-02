# Problem: Sum of Square Numbers - https://leetcode.com/problems/sum-of-square-numbers/

import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        j = floor(math.sqrt(c))
        i = 0
        while i <= j:
            val = (i ** 2) + (j ** 2)
            if val == c :
                return True
            elif val < c:
                i += 1
            elif val > c:
                j -= 1
        return False