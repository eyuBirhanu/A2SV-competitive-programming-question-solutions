# Problem: Simplify Path - https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        res = []
        for i in range(len(path)):
            if path[i] == '..' and res:
                res.pop(-1)
            elif path[i] == '..' and not res:
                pass
            elif path[i] == '.':
                pass
            elif path[i] == '':
                pass
            else:
                res.append(path[i])
        return '/'+'/'.join(res)
        