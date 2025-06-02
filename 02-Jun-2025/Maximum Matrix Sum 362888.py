# Problem: Maximum Matrix Sum - https://leetcode.com/problems/maximum-matrix-sum/description/?envType=problem-list-v2&envId=matrix

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        min_num = float('inf')
        oddCnt = 0
        total = 0
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                num = matrix[r][c]
                if num < 0:
                    oddCnt += 1
                num = abs(num)
                min_num = min(num, min_num)
                total += num

        if oddCnt % 2 != 0:
            return total - (2*min_num)
        return total 

