# Problem: Rotate Array - https://leetcode.com/problems/rotate-array/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        arr = nums.copy()
        for i in range(len(nums)):
            nums[(i+k)%len(nums)] = arr[i%len(nums)]