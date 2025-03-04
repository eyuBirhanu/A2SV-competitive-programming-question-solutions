# Problem: Happy Number - https://leetcode.com/problems/happy-number/description/

class Solution:
    def isHappy(self, n: int) -> bool:
        checker = set()
        while n not in checker:
            checker.add(n)
            to_str = str(n)
            n = 0
            for j in range(len(to_str)):
                n += int(to_str[j]) ** 2
            if n == 1:
                return True

        return False