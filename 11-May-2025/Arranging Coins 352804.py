# Problem: Arranging Coins - https://leetcode.com/problems/arranging-coins/description/

class Solution:
    def arrangeCoins(self, n: int) -> int:
        cnt = 0
        num = 0
        while n >= 0:
            num += 1
            if n - num >= 0:
                cnt += 1
            n -= num 
        return cnt
