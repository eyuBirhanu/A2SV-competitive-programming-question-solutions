# Problem: Maximum Sum of an Hourglass - https://leetcode.com/problems/maximum-sum-of-an-hourglass/

class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        res = 0
        for i in range(len(grid)-2):
            for j in range(len(grid[0]) -2):
                sub_mat = [row[j:j+3] for row in grid[i:i+3]]
                glass_sum = 0 
                for k in range(3):
                    if k == 1:
                        glass_sum += sub_mat[k][1]
                    else:
                        glass_sum += sum(sub_mat[k]) 
                res = max(glass_sum, res)
        return res
