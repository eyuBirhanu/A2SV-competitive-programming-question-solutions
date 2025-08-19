# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        range_ = []
        for i in range(0, len(sorted_nums) + 1):
           range_.append(i)
        for i in range_:
            if i not in sorted_nums:
                return i



         # if sorted_nums[i] not in range(0, len(sorted_nums)):
            #     return i 