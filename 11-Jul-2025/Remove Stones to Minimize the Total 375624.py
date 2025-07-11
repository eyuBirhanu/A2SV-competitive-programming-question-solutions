# Problem: Remove Stones to Minimize the Total - https://leetcode.com/problems/remove-stones-to-minimize-the-total/

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-x for x in piles]
        heapq.heapify(piles)
        for i in range(k):
            value = heapq.heappop(piles)
            new = -1 * (math.ceil(-1 * (value/2)))
            heapq.heappush(piles, new)
        piles = [-x for x in piles]
        return sum(piles)