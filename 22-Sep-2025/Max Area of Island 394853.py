# Problem: Max Area of Island - https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.visited = set()
        cities = 0
        rows = len(grid)
        cols = len(grid[0])

        def isBound(r, c):
            if 0 <= r < rows and 0 <= c < cols:
                return True
            return False

        def dfs(r, c):
            self.visited.add((r,c))

            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            area = 1

            for i , j in directions:
                if isBound(r+i, c+j) and (r+i, c+j) not in self.visited and grid[r+i][c+j]:
                    area += dfs(r+i, c+j)
            
            return area

        max_a = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] and (r,c) not in self.visited:
                    max_a = max(max_a ,dfs(r, c))
        return max_a
