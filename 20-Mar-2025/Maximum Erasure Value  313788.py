# Problem: Maximum Erasure Value  - https://leetcode.com/problems/maximum-erasure-value/

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        max_sum = 0
        j = 0
        numss = set()
        curr_sum = 0
        for i in range(len(nums)):
            if nums[i] not in numss:
                numss.add(nums[i])
                curr_sum += nums[i]
                max_sum = max(max_sum, curr_sum)
            else:
                while nums[i] in numss:
                    numss.remove(nums[j])
                    curr_sum -= nums[j]
                    j += 1
                numss.add(nums[i])
                curr_sum += nums[i]
                max_sum = max(max_sum, curr_sum)
        return max_sum
        