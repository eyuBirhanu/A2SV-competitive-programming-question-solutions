# Problem: Number of Provinces - https://leetcode.com/problems/number-of-provinces/

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        self.visited = set()
        provinces = 0
        l = len(isConnected)

        def dfs(i):
            self.visited.add(i)
            for j in range(l):
                if isConnected[i][j] and j not in self.visited:
                    dfs(j)
            return
        
        for i in range(l):
            if i not in self.visited:
                provinces += 1
                dfs(i)

        return provinces