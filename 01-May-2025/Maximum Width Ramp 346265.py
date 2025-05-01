# Problem: Maximum Width Ramp - https://leetcode.com/problems/maximum-width-ramp

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        max_ri = [0 for _  in nums]
        curr_max = float('-inf')
        for i in range(len(nums)-1,-1,-1):
            curr_max = max(nums[i], curr_max)
            max_ri[i] = curr_max

        max_len = float('-inf')
        l = 0
        for r in range(1, len(nums)):
            if nums[l] <= max_ri[r]:
                len_ = r - l
                max_len = max(max_len, len_)
            else:
                while l < r and nums[l] > max_ri[r]:
                    l += 1
                    if nums[l] <= max_ri[r]:
                        len_ = r - l
                        max_len = max(max_len, len_)
        return max_len