# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()

        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    grid[r][c] = 0
                    q.append((r, c))

                elif grid[r][c] == 1:
                    grid[r][c] = float('inf')

        while q:
            r, c = q.popleft()

            directions = [(r+1,c), (r-1,c), (r,c+1), (r,c-1)]

            for row , col in directions:
                if 0 <= row < rows and 0 <= col < cols and grid[row][col] > grid[r][c] +1:
                    grid[row][col] = grid[r][c] +1
                    q.append((row, col))
        max_ = 0
        for r in range(rows):
            max_r = max(grid[r])
            max_ = max(max_, max_r)
        if max_ ==  float('inf'):
            return -1
        return max_