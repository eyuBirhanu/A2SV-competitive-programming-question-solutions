# Problem: Fibonacci Number - https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, n: int) -> int:
        memo = {}
        def new(n):
            if n == 0 or n == 1:
                return n
            if n not in memo:
                memo[n] = new(n-1) + new(n-2)
            return memo[n]
        return new(n)