# Problem: Diagonal Traverse - https://leetcode.com/problems/diagonal-traverse/

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ROW = len(mat)
        COL = len(mat[0])
        res = []
        if ROW == 1:
            for i in range(COL):
                res.append(mat[0][i])
            return res

        for i in range(ROW):
            j = i
            k = 0
            sub_arr = []
            while j >= 0 and k < COL:
                sub_arr.append(mat[j][k])
                j -= 1
                k += 1
            if i % 2 == 1:
                sub_arr.reverse()
            for z in range(len(sub_arr)):
                res.append(sub_arr[z])
        
        for i in range(1, COL):
            j = ROW -1 
            k = i
            sub_arr = []
            while j >= 0 and k < COL:
                sub_arr.append(mat[j][k])
                j -= 1
                k += 1
            if (i + ROW - 1) % 2 == 1:
                sub_arr.reverse()
            for z in range(len(sub_arr)):
                res.append(sub_arr[z])

        return res