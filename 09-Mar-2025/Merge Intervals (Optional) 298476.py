# Problem: Merge Intervals (Optional) - https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        for i in range(len(intervals)):
            if not len(res):
                res.append(intervals[i])
            else:
                if res[-1][1] >= intervals[i][0] and res[-1][1] >= intervals[i][1]:
                    res[-1][1] = res[-1][1]
                elif res[-1][1] >= intervals[i][0]:
                    res[-1][1] = intervals[i][1]
                else:
                    res.append(intervals[i])
        return res
                