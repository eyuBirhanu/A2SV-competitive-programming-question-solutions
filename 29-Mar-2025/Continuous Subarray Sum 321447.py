# Problem: Continuous Subarray Sum - https://leetcode.com/problems/continuous-subarray-sum/

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        rem_map = {0:-1}
        sum_ = 0
        for i in range(len(nums)):
            sum_ += nums[i]
            rem = sum_ % k
            if rem not in rem_map:
                rem_map[rem] = i
            elif rem in rem_map:
                if i - rem_map[rem] >= 2:
                    return True
        return False                 