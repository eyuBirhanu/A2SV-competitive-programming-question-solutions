# Problem: Partition Equal Subset Sum - https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        memo = {}
        def dp(i, target):

            if i >= len(nums) or target <= 0:
                return  target == 0
                
            state = (i, target)

            if state not in memo:

                memo[state] = dp(i+1, target) or dp(i+1, target-nums[i])

            return memo[state]

        return sum(nums) % 2 == 0 and dp(0, sum(nums)//2)