# Problem: Max Increase To Keep City Skyline - https://leetcode.com/problems/max-increase-to-keep-city-skyline/

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        total_sum = 0
        row, col = len(grid), len(grid[0])
        for i in range(row):
            max_row = max(grid[i])
            max_col = 0
            for j in range(col):
                co = []
                for k in range(col):
                    co.append(grid[k][j])
                max_col = max(co)
                min_val = min(max_col, max_row)
                total_sum += (min_val - grid[i][j])
        return total_sum