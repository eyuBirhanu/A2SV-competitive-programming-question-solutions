# Problem: Maximum Number of Consecutive Values You Can Make - https://leetcode.com/problems/maximum-number-of-consecutive-values-you-can-make/description/

class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        ans = 1
        coins.sort()
        for c in coins:
            if c <= ans:
                ans += c
            else:
                break
        return ans