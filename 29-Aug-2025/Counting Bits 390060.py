# Problem: Counting Bits - https://leetcode.com/problems/counting-bits/

class Solution:
    def countBits(self, n: int) -> List[int]:
        def cnt(k):
            cnt_ = 0
            while k > 0:
                if k % 2 == 1:
                    cnt_ += 1
                k //= 2
            return cnt_
        res = []
        for i in range(n+1):
            res.append(cnt(i))
        return res
