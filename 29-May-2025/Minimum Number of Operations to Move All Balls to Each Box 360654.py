# Problem: Minimum Number of Operations to Move All Balls to Each Box - https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/description/

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        boxes = [int(n) for n in boxes]
        res = [0 for _ in range(len(boxes))]
        for b in range(len(boxes)):
            for i in range(len(boxes)):
                if boxes[i] != 0:
                    res[b] += abs((b+1) - (i+1))
        return res