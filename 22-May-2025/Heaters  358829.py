# Problem: Heaters  - https://leetcode.com/problems/heaters/

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        def target(t):
            l = 0
            r = len(heaters)-1
            min_dist = float('inf')

            while l <= r:
                mid = (l+r)//2
                min_dist = min(min_dist, abs(t-heaters[mid]))
                if heaters[mid] > t:
                    r = mid -1
                else:
                    l = mid +1
            return min_dist
           
        poss_rng = []
        for h in houses:
            poss_rng.append(target(h))
        return max(poss_rng)