# Problem: Is Subsequence - https://leetcode.com/problems/is-subsequence/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True 
        # s 
        idx = 0
        cnt = 0
        for i in range(len(t)):
            if idx >= len(s):
                return True
            if t[i] == s[idx]:
                cnt += 1
                idx += 1
        return cnt == len(s)
            