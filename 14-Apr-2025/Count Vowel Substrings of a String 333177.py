# Problem: Count Vowel Substrings of a String - https://leetcode.com/problems/count-vowel-substrings-of-a-string/description/

class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        cnt = 0
        vowels = {'a', 'e', 'i', 'o', 'u'} 
        for i in range(len(word)):
            for j in range(i+1, len(word)):
                sub_str = word[i:j+1]
                if set(sub_str) == vowels:
                    cnt += 1
        return cnt