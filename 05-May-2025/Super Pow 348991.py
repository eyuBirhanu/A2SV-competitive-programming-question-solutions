# Problem: Super Pow - https://leetcode.com/problems/super-pow/description/

class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        MOD = 1337
        i = len(b) -1
        def power(i):
            if i < 0:
                return 1
            prev = power(i-1)
            res = ((prev ** 10) * (a ** b[i])) % MOD
            return res
        return power(i)