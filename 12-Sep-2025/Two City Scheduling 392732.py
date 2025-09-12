# Problem: Two City Scheduling - https://leetcode.com/problems/two-city-scheduling/

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diff = []
        for i in range(len(costs)):
            costDiff = costs[i][1] - costs[i][0]
            val = [costDiff, costs[i][0], costs[i][1]]
            diff.append(val)
        
        diff.sort()
        half = len(costs) // 2
        ans = 0

        for i in range(len(costs)):
            if i < half:
                ans += diff[i][2]
            else:
                ans += diff[i][1]
        return ans