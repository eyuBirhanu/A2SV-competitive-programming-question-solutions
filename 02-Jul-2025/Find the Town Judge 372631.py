# Problem: Find the Town Judge - https://leetcode.com/problems/find-the-town-judge/

from collections import defaultdict
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1
        incoming = defaultdict(int)
        outgoing = defaultdict(int)
        for tr in trust:
            incoming[tr[1]] += 1
            outgoing[tr[0]] += 1
        for inc in incoming:
            if incoming[inc] == n-1 and outgoing[inc] == 0:
                return inc
        return -1
