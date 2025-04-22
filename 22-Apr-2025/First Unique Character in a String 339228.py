# Problem: First Unique Character in a String - https://leetcode.com/problems/first-unique-character-in-a-string/description/?envType=problem-list-v2&envId=queue

from collections import OrderedDict
class Solution:
    def firstUniqChar(self, s: str) -> int:
        s = list(s)
        cnt = Counter(s)
        idx = {}
        for i in range(len(s)):
            if s[i] not in idx:
                idx[s[i]] = i
        ones = OrderedDict()

        for key, value in cnt.items():
            if value == 1:
                ones[key] = value
        
        
        if len(ones) > 0:
            for key, value in ones.items():
                return idx[key]
        return -1