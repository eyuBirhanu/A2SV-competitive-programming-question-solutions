# Problem: Largest Odd Number in String - https://leetcode.com/problems/largest-odd-number-in-string/

class Solution:
    def largestOddNumber(self, num: str) -> str:
        res = ""
        for i in range(len(num)-1, -1, -1):
            if int(num[i]) % 2 == 1:
                res = num[:i+1]
                break
        return res