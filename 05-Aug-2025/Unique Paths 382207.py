# Problem: Unique Paths - https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        arr = [[0 for _ in range(n)] for _ in range(m)]
        arr[0][0] = 1
        def check(i, j):
            if 0 <= i < m and 0 <= j < n:
                return arr[i][j]
            return 0
        for r in range(m):
            for c in range(n):
                if r == 0 and c == 0:
                    continue
                arr[r][c] = check(r-1, c) + check(r, c-1)
        return arr[-1][-1]