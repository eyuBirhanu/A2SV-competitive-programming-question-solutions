# Problem: Max Consecutive Ones - https://leetcode.com/problems/max-consecutive-ones/

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0
        ones = 0
        for n in nums:
            if n == 1:
                ones += 1
            else:
                max_ones = max(max_ones, ones)
                ones = 0
        if ones > 0:
            max_ones = max(max_ones, ones)
        return max_ones