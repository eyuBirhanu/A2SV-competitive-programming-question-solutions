# Problem: Three Divisors - https://leetcode.com/problems/three-divisors/description/?envType=problem-list-v2&envId=number-theory

class Solution:
    def isThree(self, n: int) -> bool:
        factors = []
        for i in range(1 , n+1):
            if n % i == 0:
                factors.append(i)
        if len(factors) == 3:
            return True
        return False