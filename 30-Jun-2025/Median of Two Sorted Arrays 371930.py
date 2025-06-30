# Problem: Median of Two Sorted Arrays - https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        if len(nums) % 2 == 1:
            return nums[len(nums)//2]
        mid = len(nums)//2
        return ((nums[mid]) + (nums[mid-1]))/2
        