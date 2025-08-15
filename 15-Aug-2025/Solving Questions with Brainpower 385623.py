# Problem: Solving Questions with Brainpower - https://leetcode.com/problems/solving-questions-with-brainpower/

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        memo = {}
        def dp(i):
            if i >= len(questions):
                return 0
            
            if i in memo:
                return memo[i]

            memo[i] = max(dp(i+1), (questions[i][0] + dp(i+questions[i][1]+1)))

            return memo[i]

        return dp(0)
        