# Problem: Rotate String - https://leetcode.com/problems/rotate-string/

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if s == goal:
            return True
        l_s = list(s)
        l_t = list(goal)
        len_ = len(s)
        k = 0 
        while k < len_:
            new_s = [''] * len_
            for i in range(len_):
                new_s[i] = l_s[(i+k) % len_]
            if ''.join(new_s) == goal:
                return True
            k += 1
        return False
            


        