# Problem: Fibonacci Number - https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, n: int) -> int:
        memo = {}
        def dp(i):
            if i in memo:
                return memo[i]
            if i == 0 or i == 1:
                return i
            if i not in memo:
                memo[i] = dp(i - 1) + dp(i - 2)
            return memo[i]
        return dp(n)