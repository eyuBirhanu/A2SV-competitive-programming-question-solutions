# Problem: Minimum Replacements to Sort the Array - https://leetcode.com/problems/minimum-replacements-to-sort-the-array/

class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)-2, -1, -1):
            if nums[i] > nums[i+1]:
                k = (nums[i] + nums[i+1] - 1) // nums[i+1]
                ans += (k-1)
                nums[i] = nums[i] // k
        return ans