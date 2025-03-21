# Problem: Minimum Size Subarray Sum - https://leetcode.com/problems/minimum-size-subarray-sum/

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = 0
        j = 0
        sum_ = 0 
        for i in range(len(nums)):
            sum_ += nums[i]
            if sum_ >= target:
                new_arr = nums[j:i+1]
                if min_len == 0:
                    min_len = len(new_arr)
                else:
                    min_len = min(min_len, len(new_arr))
                
                while sum_ >= target and len(new_arr) > 1:
                    sum_ -= nums[j]
                    j += 1
                    if sum_ >= target:
                        new_arr2 = nums[j:i+1] 
                        if min_len == 0:
                            min_len = len(new_arr2)
                        else:
                            min_len = min(min_len, len(new_arr2))
        return min_len