# Problem: 01 Matrix - https://leetcode.com/problems/01-matrix/

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        q = deque()

        rows, cols = len(mat), len(mat[0])

        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    q.append((r, c))
                else:
                    mat[r][c] = float('inf')
        
        def isBound(r, c):
            if 0 <= r < rows and 0 <= c < cols:
                return True
            return False
        
        while q:
            r, c = q.popleft()
            directions = [(1,0), (-1,0), (0,1), (0,-1)]

            for i ,j in directions:
                if isBound(r+i, c+j) and mat[r+i][c+j] > mat[r][c] +1:
                    mat[r+i][c+j] = mat[r][c] +1

                    q.append((r+i, c+j))

        return mat
