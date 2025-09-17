# Problem: Jump Game - https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        canJump = 0

        for i in range(len(nums)):
            if i > canJump:
                return False
            
            if nums[i] + i > canJump:
                canJump = nums[i] + i

            if canJump >= len(nums)-1:
                return True

            