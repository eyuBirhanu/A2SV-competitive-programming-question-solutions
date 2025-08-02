# Problem: Climbing Stairs - https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        # l
        cnt = 0
        def dp(n):
            if n in memo:
                return memo[n]
            if n == 0 or n == 1:
                return 1
            memo[n] = dp(n-1) + dp(n-2) 
            return memo[n]
        return dp(n)