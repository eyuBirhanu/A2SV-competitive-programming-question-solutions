# Problem: Word search - https://leetcode.com/problems/word-search/

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0]) 
        visit = set()

        def check(r, c, curr):
            if curr == len(word):
                return True

            if (not (0 <= r < row and 0 <= c < col) or
                (r, c) in visit or
                board[r][c] != word[curr]):
                return False
                
            visit.add((r, c))
            res = (check(r+1, c, curr+1) or
                    check(r-1, c, curr+1) or
                    check(r, c+1, curr+1) or
                    check(r, c-1, curr+1))
            visit.remove((r,c))
            return res


        
        for r in range(row):
            for c in range(col):
                if check(r, c, 0): return True
        return False