# Problem: Longest Substring Without Repeating Characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        j = 0
        sub_str = set()
        for i in range(len(s)):
            if s[i] not in sub_str:
                sub_str.add(s[i])
                max_len = max(max_len, len(sub_str))
            else:
                while j < i and s[j] != s[i]:
                    if s[j] in sub_str:
                        sub_str.remove(s[j])
                    j += 1
                if s[j] == s[i]:
                    j += 1
                sub_str.add(s[i])
                max_len = max(max_len, len(sub_str))
        return max_len
