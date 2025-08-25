# Problem: Single Number - https://leetcode.com/problems/single-number/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = Counter(nums)
        for key, value in count.items():
            if value == 1:
                return key