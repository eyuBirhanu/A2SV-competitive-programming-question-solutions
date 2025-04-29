# Problem: Score of Parentheses - https://leetcode.com/problems/score-of-parentheses/

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        store = []
        cnt = 0
        for c in s:
            if c == '(':
                store.append(c)
            else:
                if store[-1] == '(':
                    store[-1] = 1
                else:
                    val = 0
                    while store[-1] != '(':
                        val += store[-1]
                        store.pop()
                    store.append(val)
                    store[-1] *= 2 
                    store.pop(-2)
        return sum(store)
            
        