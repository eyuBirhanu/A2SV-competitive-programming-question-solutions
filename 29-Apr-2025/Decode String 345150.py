# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        store = []
        for c in s:
            if c != ']':
                store.append(c)
            else:
                inside = ''
                while store[-1] != '[':
                    inside += store.pop()
                store.pop()
                inside = inside[::-1]
                k = ''
                while store and store[-1].isdigit():
                    k += store.pop()
                k = int(k[::-1])
                str_ = k * inside
                for c in str_:
                    store.append(c)
        return ''.join(store)
                
        