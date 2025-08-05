# Problem: House Robber - https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def dp(i):
            if i == 0:
                return nums[i]
            if i == 1:
                return max(nums[0], nums[1])
            if i not in memo:
                memo[i] = max(dp(i-1), dp(i-2)+nums[i])
            return memo[i]
        return dp(len(nums)-1)