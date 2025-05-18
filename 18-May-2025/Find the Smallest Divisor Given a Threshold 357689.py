# Problem: Find the Smallest Divisor Given a Threshold - https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def check(k):
            val = 0
            for i in nums:
                val += math.ceil(i/k)
            return val
        
        l = 1
        r = max(nums)
        while l < r:
            mid = (l+r)//2
            if check(mid) <= threshold:
                r = mid
            else:
                l = mid +1
        return l