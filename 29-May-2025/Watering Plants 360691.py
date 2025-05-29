# Problem: Watering Plants - https://leetcode.com/problems/watering-plants/

class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        init = capacity
        steps = 0
        for p in range(len(plants)):
            if capacity < plants[p]:
                steps += (2*p)
                capacity = init

            steps += 1
            capacity -= plants[p]
        return steps
