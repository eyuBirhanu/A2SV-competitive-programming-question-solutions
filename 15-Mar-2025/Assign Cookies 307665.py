# Problem: Assign Cookies - https://leetcode.com/problems/assign-cookies

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        final = []
        i = 0
        j = 0
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                final.append(g[i])
                j += 1
                i += 1
            elif s[j] < g[i]:
                j += 1
        if len(final) > len(s):
            return len(s)
        else:
            return len(final)
        
       