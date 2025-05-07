# Problem: Koko Eating Bananas - https://leetcode.com/problems/koko-eating-bananas/

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def possible(k):
            total = 0
            for p in piles:
                total += math.ceil(p/k)
            return total <= h

        l = 1
        r = max(piles)
        while l <= r:
            mid = (l+r) // 2
            if possible(mid):
                r = mid -1
            else:
                l = mid +1
        return l

        