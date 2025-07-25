# Problem: Letter Combinations of a Phone Number - https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return [] 
        keyboard = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        res = []

        def back(comb , i):
            if len(comb) == len(digits):
                res.append(''.join(comb))
                return

            for j in keyboard[digits[i]]:
                comb.append(j)
                back(comb, i+1) 
                comb.pop() 
        
        back([], 0)
        return res
            
        
