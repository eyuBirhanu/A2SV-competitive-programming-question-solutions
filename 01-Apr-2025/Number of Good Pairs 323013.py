# Problem: Number of Good Pairs - https://leetcode.com/problems/number-of-good-pairs/

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = Counter(nums)
        list_ = list(count.values()) 
        cnt  = 0
        for i in range(len(list_)):
            n = list_[i] 
            cnt += (n * (n -1)//2)
        return cnt
