# Problem: Island Perimeter - https://leetcode.com/problems/island-perimeter/description/

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        
        p = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    sub_p = 4
                    if r > 0 and grid[r-1][c] == 1:
                        sub_p -= 1
                    if r < ROWS-1 and grid[r+1][c] == 1:
                        sub_p -= 1
                    if c > 0 and grid[r][c-1] == 1:
                        sub_p -= 1
                    if c < COLS-1 and grid[r][c+1] == 1:
                        sub_p -= 1
                    p += sub_p
        return p