# Problem: N-th Tribonacci Number - https://leetcode.com/problems/n-th-tribonacci-number/description/

class Solution:
    def tribonacci(self, n: int) -> int:
        tri = [0, 1, 1]
        if n < 2:
            return tri[n] 
        for i in range(2, n):
            tri.append(sum([tri[-1], tri[-2], tri[-3]]))
        return tri[-1]