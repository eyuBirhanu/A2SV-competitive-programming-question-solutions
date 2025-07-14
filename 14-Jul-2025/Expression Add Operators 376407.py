# Problem: Expression Add Operators - https://leetcode.com/problems/expression-add-operators/description/

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []
        def dfs(poss, exp):
            if poss == len(num):
                if eval(exp) == target:
                    res.append(exp)
                return 
            for i in range(poss+1, len(num)+1):
                temp = num[poss:i]
                if len(temp) > 1 and temp[0] == '0':
                    return
                if poss == 0:
                    dfs(i, temp)
                else:
                    dfs(i, exp + '+' + temp)
                    dfs(i, exp + '*' + temp)
                    dfs(i, exp + '-' + temp)
            # return 
        dfs(0, '')
        return res