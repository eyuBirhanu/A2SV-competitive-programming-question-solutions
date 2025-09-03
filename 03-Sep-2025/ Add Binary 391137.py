# Problem:  Add Binary - https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if a == '0' and b == '0' :
            return '0'
        def toBi(str_):
            x = 0
            cnt = len(str_)-1
            for i in str_:
                x += (2**cnt) * int(i)
                cnt -= 1
            return x
        # uiuiuu
        a = toBi(a)
        b = toBi(b)
        c = a + b
        res = ''

        while c > 0 :
            res += str(c%2)
            c //= 2
        return res[::-1]