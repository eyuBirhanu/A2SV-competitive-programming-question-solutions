# Problem: Combinations - https://leetcode.com/problems/combinations/

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        def dfs(i):
            if len(t) == k:
                ans.append(t[:])
                return
            if i > n:
                return
            t.append(i) 
            dfs(i+1)
            t.pop()
            dfs(i+1)
        ans = []
        t = []
        dfs(1)
        return ans