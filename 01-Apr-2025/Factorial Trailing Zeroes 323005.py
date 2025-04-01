# Problem: Factorial Trailing Zeroes - https://leetcode.com/problems/factorial-trailing-zeroes/

class Solution:
    def trailingZeroes(self, n: int) -> int:
        def facto(x):
            fact_num = 1
            for i in range(1,n+1):
                fact_num = fact_num * i
            return fact_num
        res = facto(n)
        cnt = 0
        working = True
        while working:
            if res % 10 == 0:
                res //= 10
                cnt += 1
            else:
                working = False
        return cnt
            