# Problem: Find the Difference - https://leetcode.com/problems/find-the-difference/

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_cnt = Counter(s)
        t_cnt  = Counter(t)
        res = ''
        for item, value in t_cnt.items():
            if item in s_cnt and item in t_cnt:
                t_cnt[item] -= s_cnt[item]
                res += (item * t_cnt[item])
            else:
                res += item
        return res