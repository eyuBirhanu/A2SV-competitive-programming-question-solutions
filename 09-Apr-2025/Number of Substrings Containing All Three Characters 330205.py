# Problem: Number of Substrings Containing All Three Characters - https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/description/

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        cnt = 0
        lett = {'a':0, 'b':0, 'c':0}
        j = 0
        for i in range(len(s)):
            lett[s[i]] += 1
            if all(value >= 1 for value in lett.values()):
                cnt += len(s) - i  
                while j < i and all(value >= 1 for value in lett.values()):
                    lett[s[j]] -= 1
                    j += 1
                    if all(value >= 1 for value in lett.values()):
                        cnt += len(s) - i 
        return cnt
        