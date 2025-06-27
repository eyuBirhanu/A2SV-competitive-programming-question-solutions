# Problem: Splitting a String Into Descending Consecutive Values - https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/

class Solution:
    def splitString(self, s: str) -> bool:

        def backtrack(first, j):
            if j >= len(s):
                return True
            for k in range(j, len(s)):
                second = int(s[j:k+1])
                if second == first-1 and backtrack(second, k+1):
                    return True
                

        for i in range(len(s)-1):
            first = int(s[:i+1])
            if backtrack(first, i+1):
                return True
        return False
        