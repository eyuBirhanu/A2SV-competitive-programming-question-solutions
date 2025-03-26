# Problem: Find the Maximum Achievable Number - https://leetcode.com/problems/find-the-maximum-achievable-number/description/

class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        x = num
        for i in range(t):
            x += 2
        return x
        