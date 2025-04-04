# Problem: Squares of a Sorted Array
(Easy) - https://leetcode.com/problems/squares-of-a-sorted-array/

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        stack = []
        for num in nums:
            num *= num
            stack.append(num)
        return sorted(stack)
        