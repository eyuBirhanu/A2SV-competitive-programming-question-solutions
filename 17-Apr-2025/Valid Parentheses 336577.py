# Problem: Valid Parentheses - https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        Parentheses = {")": "(",
                  "]": "[",
                  "}": "{"}
        stack = []
        for char in s:
            if char in Parentheses:
                if stack != [] and stack[-1] == Parentheses[char]:
                    stack.pop(-1)
                else:
                    return False
            else:
                stack.append(char)
        if stack == []:
            return True
        