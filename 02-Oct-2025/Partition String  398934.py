# Problem: Partition String  - https://leetcode.com/problems/partition-string/description/

class Solution:
    def partitionString(self, s: str) -> List[str]:
        segemnt = ''

        seen = set()

        res = []

        for c in s:
            segemnt += c
            if segemnt in seen:
                continue
            seen.add(segemnt)
            res.append(segemnt)
            segemnt = ''
        return res