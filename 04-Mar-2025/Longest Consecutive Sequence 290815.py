# Problem: Longest Consecutive Sequence - https://leetcode.com/problems/longest-consecutive-sequence/description/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        num_set = set(nums)
        for i in num_set:
            if (i-1) not in num_set:
                j = 1
                while (i+j) in num_set:
                    j += 1
                res = max(res, j)
        return res