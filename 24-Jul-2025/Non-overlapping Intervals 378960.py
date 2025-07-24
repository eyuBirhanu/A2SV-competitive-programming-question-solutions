# Problem: Non-overlapping Intervals - https://leetcode.com/problems/non-overlapping-intervals/description/

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x : x[1])
        cnt = 0
        store = []
        for i in range(len(intervals)):
            if i == 0:
                store.append(intervals[i])
                continue
            if store[-1][1] > intervals[i][0]:
                cnt += 1
            else:
                store.append(intervals[i])
            
        return cnt
