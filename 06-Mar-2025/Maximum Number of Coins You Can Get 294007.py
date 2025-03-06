# Problem: Maximum Number of Coins You Can Get - https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        i = 0
        j = len(piles)
        sum_ = 0 
        while i < j:
            sum_ += piles[j-2]
            i +=1 
            j -= 2
        return sum_
