# Problem: Fibonacci Number - https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, n: int) -> int:
        arr = [0, 1]
        if n < 2:
            return n
        
        for i in range(n-1):
            res = arr[-1] + arr[-2]
            arr.append(res)
        return arr[-1]
        # 0 1 1