# Problem: Find Right Interval - https://leetcode.com/problems/find-right-interval/

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        idx = {}
        for i in range(len(intervals)):
            idx[intervals[i][0]] = i
        arr = deepcopy(intervals)
        arr.sort()
        
        def finder(k):
            l = 0
            r = len(arr)-1
            res = float('-inf')
            while l <= r:
                mid = (l+r)//2
                if arr[mid][0] >= k:
                    res = arr[mid][0]
                    r = mid -1
                else:
                    l = mid +1
            if res in idx:
                return idx[res]
            return -1
        
        

        res = [0 for _ in range(len(intervals))]
        for i in range(len(intervals)):
            res[i] = finder(intervals[i][1])
        return res
        