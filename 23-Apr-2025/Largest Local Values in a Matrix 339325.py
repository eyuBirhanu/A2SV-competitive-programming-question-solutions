# Problem: Largest Local Values in a Matrix - https://leetcode.com/problems/largest-local-values-in-a-matrix/

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        row, col = len(grid), len(grid[0])
        res = [[0 for _ in range(col-2)] for _ in range(row-2)]
        r, c = 0, 0 
        while r < row-2:
            c = 0
            while c < col-2:
                max_val = 0
                for i in range(3):
                    for j in range(3):
                        max_val = max(max_val, grid[r+i][c+j])
                res[r][c] = max_val
                c += 1
            r += 1
        return res