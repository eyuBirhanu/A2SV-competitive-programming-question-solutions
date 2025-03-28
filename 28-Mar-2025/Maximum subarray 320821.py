# Problem: Maximum subarray - https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        sum_ = 0
        j = 0
        for i in range(len(nums)):
            sum_ += nums[i]
            if sum_ < 0:
                max_sum = max(sum_, max_sum)
                sum_ = 0
            elif sum_ > 0:
                max_sum = max(max_sum, sum_)
            elif sum_ == 0:
                max_sum = max(max_sum, sum_) 
        return max_sum