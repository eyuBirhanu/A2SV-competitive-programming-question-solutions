# Problem: K-th Symbol in Grammar - https://leetcode.com/problems/k-th-symbol-in-grammar/description/

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        curr = 0
        l, r = 1, 2**(n-1)

        for _ in range(n-1):
            mid = (l+r)//2
            if k <= mid:
                r = mid
            else:
                l = mid +1
                if curr:
                    curr = 0
                else:
                    curr = 1
        return curr
        