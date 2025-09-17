# Problem: Get Maximum in Generated Array - https://leetcode.com/problems/get-maximum-in-generated-array/description/

class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        nums = [0 for _ in range(n+1)] 
        if n >= 1:
            nums[1] = 1

        for i in range(n//2+1):
            nums[2 * i] = nums[i]
            if 2*i+1 <= n:
                nums[2 * i + 1] = nums[i] + nums[i+1]
        return max(nums)