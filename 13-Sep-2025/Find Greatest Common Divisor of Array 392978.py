# Problem: Find Greatest Common Divisor of Array - https://leetcode.com/problems/find-greatest-common-divisor-of-array/

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        def gcd(a,b):
            if b == 0:
                # srstyjstjyyk,uy
                return a
            return gcd(b, a%b)

        nums.sort()
        return gcd(nums[0], nums[-1])