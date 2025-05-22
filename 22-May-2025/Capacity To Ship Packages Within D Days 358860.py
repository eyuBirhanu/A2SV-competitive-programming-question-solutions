# Problem: Capacity To Ship Packages Within D Days - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def capacityChk(capacity):
            ship = 0
            cnt = 0
            for w in weights:
                ship += w
                if ship > capacity:
                    cnt += 1
                    ship = 0
                    ship += w
            if ship > 0:
                cnt += 1
            if cnt <= days:
                return True
            else:
                return False
        
        l = max(weights)
        r = sum(weights)
        while l <= r:
            mid = (l+r)//2
            if capacityChk(mid):
                r = mid -1
            else:
                l = mid +1
        return l
        

        