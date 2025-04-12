# Problem: Minimum Operations to Reduce X to Zero - https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/description/

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        if x == 0:
            return 0
        sum_ = sum(nums)
        target = sum_ - x
        minOp = float('inf')

        preSum = 0
        j = 0
        for i in range(len(nums)):
            preSum += nums[i]
            if preSum == target:
                val = j + (len(nums) - (i+1))
                minOp = min(minOp, val)
            else:
                while j <= i and preSum > target:
                    preSum -= nums[j]
                    j += 1
                    if preSum == target:
                        val = j + (len(nums) - (i+1))
                        minOp = min(minOp, val)
        if minOp == float('inf'):
            return -1
        else:
            return minOp