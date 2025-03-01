# Problem: Row With Maximum Ones - https://leetcode.com/problems/row-with-maximum-ones/

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        ROW = len(mat)
        COL = len(mat[0])
        res = [0, 0]

        for i in range(ROW):
            count = 0
            for j in range(COL):
                if mat[i][j] == 1:
                    count += 1
            if count > res[1]:
                res[0] = i
                res[1] = count
        return res