# Problem: Generate Parentheses - https://leetcode.com/problems/generate-parentheses/description/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        str_ = []
        ans = []
        def dfs(lCnt, rCnt):
            
            if lCnt == n and rCnt == n:
                ans.append(''.join(str_))
                return
            
            if lCnt < n:
                str_.append('(')
                dfs(lCnt+1, rCnt)
                str_.pop()

            if rCnt < lCnt :
                str_.append(')')
                dfs(lCnt, rCnt+1)
                str_.pop()

        dfs(0, 0)
        return ans
            