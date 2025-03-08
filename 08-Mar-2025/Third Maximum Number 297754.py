# Problem: Third Maximum Number - https://leetcode.com/problems/third-maximum-number/description/

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        numbers = list(set(nums))
        numbers.sort()
        
        if len(numbers) < 3:
            return numbers[-1]
        else:
            return numbers[-3]