# Problem: Map of Highest Peak - https://leetcode.com/problems/map-of-highest-peak/description/

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        q = deque()

        rows, cols = len(isWater), len(isWater[0])

        for r in range(rows):
            for c in range(cols):
                if isWater[r][c] == 1:
                    isWater[r][c] = 0
                    q.append((r, c)) 
                else:
                    isWater[r][c] = float('inf')
        

        while q:
            r, c = q.popleft()
            directions = [(r+1,c), (r-1,c), (r,c+1), (r,c-1)]

            for row, col in directions:
                if 0 <= row < rows and 0 <= col < cols and isWater[row][col] > isWater[r][c] +1:
                    isWater[row][col] = isWater[r][c] +1
                    q.append((row, col))
        return isWater