# Problem: Number of Islands - https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        visited = set()
        isLands = 0

        def inBound(r, c):
            return 0 <= r < rows and 0 <= c < cols

        def bfs(r, c):
            q = deque()

            q.append((r, c))
            visited.add((r, c))

            while q:
                r, c = q.popleft()
                if inBound(r+1, c) and (r+1, c) not in visited and grid[r+1][c] == '1':
                    q.append((r+1, c))
                    visited.add((r+1, c))

                if inBound(r-1, c) and (r-1, c) not in visited and grid[r-1][c] == '1':
                    q.append((r-1, c))
                    visited.add((r-1, c))

                if inBound(r, c+1) and (r, c+1) not in visited and grid[r][c+1] == '1':
                    q.append((r, c+1))
                    visited.add((r, c+1))

                if inBound(r, c-1) and (r, c-1) not in visited and grid[r][c-1] == '1':
                    q.append((r, c-1))
                    visited.add((r, c-1))
                
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visited:
                    bfs(r, c)
                    isLands += 1
        return isLands

