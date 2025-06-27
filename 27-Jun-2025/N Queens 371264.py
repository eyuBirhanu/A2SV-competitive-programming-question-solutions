# Problem: N Queens - https://leetcode.com/problems/n-queens/

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        grid = [['.']*n for _ in range(n)]
        
        def dfs(r, cols, diag1, diag2):
            if r == n:
                temp = ["".join(r) for r in grid]
                ans.append(temp)
                return 
            for c in range(n):
                if c in cols or (c+r) in diag1 or (r-c) in diag2:
                    continue
                cols.add(c)
                diag1.add(c+r)
                diag2.add(r-c)
                grid[r][c] = "Q"

                dfs(r+1, cols, diag1, diag2)
                
                cols.remove(c)
                diag1.remove(c+r)
                diag2.remove(r-c)
                grid[r][c] = "."

        dfs(0, set(), set(), set())
        return ans
                