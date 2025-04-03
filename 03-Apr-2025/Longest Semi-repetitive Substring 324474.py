# Problem: Longest Semi-repetitive Substring - https://leetcode.com/problems/find-the-longest-semi-repetitive-substring/

class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        max_len = 0
        if len(s) == 1:
            return 1 
        for i in range(len(s)):
            found = False
            for j in range(i+1, len(s)):
                sub_str = s[i:j+1]
                if sub_str[-1] == sub_str[-2] and not found:
                    max_len = max(max_len, len(sub_str))
                    found = True
                elif sub_str[-1] == sub_str[-2] and found:
                    max_len = max(max_len, len(sub_str)-1)
                    break
                else:
                    max_len = max(max_len, len(sub_str))

        return max_len
        