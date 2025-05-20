# Problem: 132 Pattern - https://leetcode.com/problems/132-pattern/

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        min_ = nums[0]
        res = []
        for n in nums[1:]:
            while res and n >= res[-1][0]:
                res.pop()
            if res and n > res[-1][1]:
                return True

            res.append([n, min_])
            min_ = min(min_, n)
        return False
        