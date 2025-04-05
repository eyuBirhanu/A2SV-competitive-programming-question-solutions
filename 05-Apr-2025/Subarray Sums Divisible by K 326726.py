# Problem: Subarray Sums Divisible by K - https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        rmd = {0:1} 
        ans = 0
        curr_sum = 0
        for num in nums:
            curr_sum += num
            remain = curr_sum % k
            if remain in rmd:
                ans += rmd[remain]
                rmd[remain] += 1
            else:
                rmd[remain] = 1
        return ans