# Problem: Find Kth Bit in Nth Binary String - https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def create(n, s):
            if n == 0:
                return s
            res = ''
            for i in s:
                if i == '0':
                    res += '1'
                else:
                    res += '0'
            str_ = s + '1' + res[::-1]
            return create(n-1, str_)
        result = create(n-1, '0')
        return result[k-1]


        