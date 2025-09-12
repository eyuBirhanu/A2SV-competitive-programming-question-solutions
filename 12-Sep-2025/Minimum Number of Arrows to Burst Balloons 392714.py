# Problem: Minimum Number of Arrows to Burst Balloons - https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x : x[1])
        ans = len(points)
        inter = points[0][1]
        print(points)
        for i in range(1, len(points)):
            if points[i][0] > inter:
                inter = points[i][1]
            else:
                ans -= 1
        return ans