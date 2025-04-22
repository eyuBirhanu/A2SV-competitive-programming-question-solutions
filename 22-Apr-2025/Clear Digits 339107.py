# Problem: Clear Digits - https://leetcode.com/problems/clear-digits/description/

class Solution:
    def clearDigits(self, s: str) -> str:
        store = []
        for i in range(len(s)):
            if s[i].isdigit():
                store.pop()
            else:
                store.append(s[i])
        return "".join(store)
        