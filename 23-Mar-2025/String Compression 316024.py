# Problem: String Compression - https://leetcode.com/problems/string-compression/

class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            return 1
        write = 0

        i = 0
        while i < len(chars):
            j = 1
            while i + j < len(chars) and chars[i+j] == chars[i]:
                j += 1
            chars[write] = chars[i]
            write += 1

            if j > 1:
                str_ = str(j) 
                chars[write:write+len(str_)] = list(str_)
                write += len(str_)
            i += j
        return write