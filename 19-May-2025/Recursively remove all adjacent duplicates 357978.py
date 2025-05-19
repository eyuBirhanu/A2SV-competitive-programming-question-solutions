# Problem: Recursively remove all adjacent duplicates - https://www.geeksforgeeks.org/recursively-remove-adjacent-duplicates-given-string/

#User function Template for python3

class Solution:
    def removeUtil (self, S):
        res = ''
        len_ = len(S)
        i = 0
        
        while i < len_:
            repeat = False 
            while i+1 < len_ and S[i] == S[i+1]:
                repeat = True
                i += 1
            if not repeat:
                res += S[i]
            i += 1
        if len_ != len(res):
            return self.removeUtil(res)
        return res