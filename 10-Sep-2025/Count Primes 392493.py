# Problem: Count Primes - https://leetcode.com/problems/count-primes/

class Solution:
    def countPrimes(self, n: int) -> int:
            # ff
        isPrime = [True for i in range(n)]
        if n > 0: isPrime[0] = False
        if n > 1: isPrime[1] = False
        
        i = 2
        while i * i < n:
            if isPrime[i]:
                j = i * i
                while j < n:
                    isPrime[j] = False
                    j += i
            i += 1
        count = Counter(isPrime)
        return count[True]