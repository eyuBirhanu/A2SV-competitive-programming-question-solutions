# Problem: Target Sum - https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        def dfs(idx, total):
            if idx == len(nums):
                if total  == target:
                    return 1
                return 0

            if (idx, total) in dp:
                return dp[(idx, total)]

            dp[(idx, total)] = (dfs(idx+1, total+nums[idx]) + 
                                dfs(idx+1, total-nums[idx]))

            return dp[(idx, total)]
        return dfs(0, 0)