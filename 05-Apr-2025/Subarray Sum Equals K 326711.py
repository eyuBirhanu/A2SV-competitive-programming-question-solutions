# Problem: Subarray Sum Equals K - https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sums = {0:1} 
        cnt = 0
        sum_ = 0
        for num in nums:
            sum_ += num
            pre_sum = sum_ - k
            if pre_sum in sums:
                cnt += sums[pre_sum]
            
            if sum_ in sums:
                sums[sum_] += 1
            else:
                sums[sum_] = 1
        return cnt