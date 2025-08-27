# Problem: Combination Sum IV - https://leetcode.com/problems/combination-sum-iv/description/

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}
        
        def dp(sum_):
            if sum_ > target:
                return 0
            if sum_ == target:
                return 1

            if sum_ in memo:
                return memo[sum_]
            total = 0
            for num in nums:
                total += dp(sum_ + num)
                memo[sum_] = total

            return memo[sum_]
            
        return dp(0)
             
