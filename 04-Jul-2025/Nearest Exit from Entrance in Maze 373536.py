# Problem: Nearest Exit from Entrance in Maze - https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/

class Solution(object):
    def nearestExit(self, maze, entrance):
        q = deque()
        visited = set()
        q.append((tuple(entrance), None, 0))

        def is_not_valid(i, j):
            return i < 0 or j < 0 or i >= len(maze) or j >= len(maze[0])

        while q:
            cell, prev, d = q.popleft()
            i, j = cell

            if (cell in visited or
             (not is_not_valid(i, j) and maze[i][j] == "+" )):
              continue
            if is_not_valid(i, j):
                if prev != tuple(entrance): return d - 1
                continue

            visited.add(cell)

            q.append(((i+1, j), cell, d+1))
            q.append(((i-1, j), cell, d+1))
            q.append(((i, j+1), cell, d+1))
            q.append(((i, j-1), cell, d+1))

        return -1