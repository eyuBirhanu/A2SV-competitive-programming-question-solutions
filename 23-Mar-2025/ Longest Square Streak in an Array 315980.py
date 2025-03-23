# Problem:  Longest Square Streak in an Array - https://leetcode.com/problems/longest-square-streak-in-an-array/description/?envType=problem-list-v2&envId=sorting

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        numbers = set(nums)
        max_len = 0 

        nums = list(numbers)
        for i in range(len(nums)):
            cnt = 1
            num = nums[i] ** 2
            while cnt < len(nums) and num in numbers:
                num = num ** 2
                cnt += 1
            max_len = max(max_len, cnt)
        if max_len < 2:
            return -1
        else:
            return max_len