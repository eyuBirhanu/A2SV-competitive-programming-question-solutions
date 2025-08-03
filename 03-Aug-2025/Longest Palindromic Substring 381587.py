# Problem: Longest Palindromic Substring - https://leetcode.com/problems/longest-palindromic-substring/description/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        # res 
        if len(s) == 1:
            return s
        for i in range(len(s)):
            if i < 1:
                res = s[:i+1]
            elif i > 0:
                l, r = i-1, i+1
                while l >= 0 and r < len(s):
                    if s[l] == s[r]:
                        sub_res = s[l:r+1]
                        if len(sub_res) > len(res):
                            res = sub_res
                        l -= 1
                        r += 1
                    else:   
                        break
                l, r = i-1, i
                while l >= 0 and r < len(s):
                    if s[l] == s[r]:
                        sub_res = s[l:r+1]
                        if len(sub_res) > len(res):
                            res = sub_res
                        l -= 1
                        r += 1
                    else:   
                        break
                
        return res
                