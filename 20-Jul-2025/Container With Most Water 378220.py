# Problem: Container With Most Water - https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        # 1002
        right = len(height)-1
        max_area = 0
        while left < right:
            curr_area = (right - left) * min(height[left], height[right])
            max_area = max(max_area, curr_area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area