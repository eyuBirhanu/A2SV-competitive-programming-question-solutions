# Problem: Count Good Numbers - https://leetcode.com/problems/count-good-numbers/

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        def power(b, e):
            if e == 0:
                return 1
            res = power(b, e // 2)
            res *= res
            res %= MOD
            if e%2: res *= b
            res %= MOD
            return res
        
        return (power(5, (n+1)//2) * power(4, (n//2))) % MOD
