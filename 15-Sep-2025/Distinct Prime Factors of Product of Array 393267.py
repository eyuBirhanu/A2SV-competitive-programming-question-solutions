# Problem: Distinct Prime Factors of Product of Array - https://leetcode.com/problems/distinct-prime-factors-of-product-of-array/

class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        res = set() 

        def prime_factors(n):
            factors = set()
            while n % 2 == 0:
                factors.add(2)
                n //= 2  

            i = 3
            while i * i <= n:
                while n % i == 0:
                    factors.add(i)
                    n //= i
                i += 2

            if n > 2:
                factors.add(n)

            return factors
        for n in nums:
            num = prime_factors(n)
            for i in num:
                res.add(i)
        return len(res)