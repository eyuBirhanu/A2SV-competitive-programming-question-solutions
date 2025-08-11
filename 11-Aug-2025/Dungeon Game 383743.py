# Problem: Dungeon Game - https://leetcode.com/problems/dungeon-game/

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        row = len(dungeon)
        col = len(dungeon[0])

        def valid(r, c):
            if 0 <= r < row and 0 <= c < col:
                return dungeon[r][c]
            return float('-inf')

        for r in range(row-1, -1, -1):
            for c in range(col-1, -1, -1):
                right = valid(r, c+1)
                bottom = valid(r+1, c)
                if bottom == float('-inf') and right == float('-inf'):
                    if dungeon[r][c] > 0:
                        dungeon[r][c] = 0 
                    continue
                if bottom == float('-inf') and right:
                    if dungeon[r][c] + right > 0:
                        dungeon[r][c] = 0
                    else:
                        dungeon[r][c] += right
                elif right == float('-inf') and bottom:
                    if dungeon[r][c] + bottom > 0:
                        dungeon[r][c] = 0
                    else:
                        dungeon[r][c] += bottom
                else:
                    dungeon[r][c] += max(right, bottom) 
                
                if dungeon[r][c] > 0:
                     dungeon[r][c] = 0 
                # print(dungeon)
        if dungeon[0][0] > 0:
            return 1
        return abs(dungeon[0][0]) +1 