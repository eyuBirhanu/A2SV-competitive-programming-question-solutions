# Problem: Last Stone Weight - https://leetcode.com/problems/last-stone-weight/

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            fir = heapq.heappop(stones)
            sec = heapq.heappop(stones)
            if fir != sec:
                new = -1 * ((-1*fir) - (-1*sec))
                heapq.heappush(stones , new)
        if stones:
            return -1 *stones[0] 
        return 0
