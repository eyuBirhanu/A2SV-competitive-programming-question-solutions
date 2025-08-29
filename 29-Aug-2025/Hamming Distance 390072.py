# Problem: Hamming Distance - https://leetcode.com/problems/hamming-distance/

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        z = x ^ y
        cnt = 0

        while z > 0:
            if z % 2 == 1:
                cnt += 1
            z //= 2
        return cnt
