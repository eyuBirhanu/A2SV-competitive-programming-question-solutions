# Problem: Non-decreasing Array - https://leetcode.com/problems/non-decreasing-array/

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        count = 0
        for i in range(len(nums)-1):
            if nums[i] <= nums[i+1]:
                continue
            if count > 1:
                return False
            if i == 0 or nums[i+1] >= nums[i-1]:
                nums[i] = nums[i+1]
            else:
                nums[i+1] = nums[i]
            count += 1
        if count <= 1:
            return True
        else:
            return False