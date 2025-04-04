# Problem: Height Checker
(Easy) - https://leetcode.com/problems/height-checker/

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        height = sorted(heights)
        cnt = 0
        for i in range(len(heights)):
            if heights[i] != height[i]:
                cnt += 1
        return cnt
        