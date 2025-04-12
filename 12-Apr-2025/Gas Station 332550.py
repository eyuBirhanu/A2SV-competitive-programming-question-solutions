# Problem: Gas Station - https://leetcode.com/problems/gas-station/

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        for i in range(len(gas)):
            gas[i] = gas[i] - cost[i]
        start = 0
        total = 0
        for i in range(len(gas)):
            total += gas[i]
            if total < 0:
                total = 0
                start = i+1
        return start