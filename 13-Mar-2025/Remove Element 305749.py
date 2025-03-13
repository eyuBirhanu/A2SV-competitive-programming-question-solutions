# Problem: Remove Element - https://leetcode.com/problems/remove-element/description/

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for x in range(len(nums)):
            if nums[x] != val:
                nums[i] = nums[x]
                i += 1 
        return i 