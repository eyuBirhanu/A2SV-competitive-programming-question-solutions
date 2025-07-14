# Problem: Kth Smallest Element in a Sorted Matrix - https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        row = len(matrix)
        col = len(matrix[0])
        for i in range(len(matrix)):
            heapq.heappush(heap, (matrix[i][0], i, 0))
        cnt = 0
        res = []
        while heap and cnt < k:
            val, r, c = heapq.heappop(heap)
            res.append(val)
            if c+1 < col:
                heapq.heappush(heap,(matrix[r][c+1], r, c+1))
            cnt += 1
        return res[-1]