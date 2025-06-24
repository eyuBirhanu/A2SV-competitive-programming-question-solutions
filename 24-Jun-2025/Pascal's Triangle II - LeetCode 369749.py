# Problem: Pascal's Triangle II - LeetCode - https://leetcode.com/problems/pascals-triangle-ii/

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        starter = [1]
        for i in range(rowIndex):
            new = [0 for i in range(len(starter)+1)]
            for j in range(len(starter)):
                new[j] += starter[j]
                new[j+1] += starter[j]

            starter = new
        return starter
            