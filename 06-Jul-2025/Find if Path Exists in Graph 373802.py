# Problem: Find if Path Exists in Graph - https://leetcode.com/problems/find-if-path-exists-in-graph/

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node, visited):
            if node == destination:
                return True
            
            visited.add(node)
            for adj in graph[node]:
                if adj not in visited:
                    found =  dfs(adj, visited)

                    if found:
                        return True
        visited = set()
        if dfs(source, visited):
            return True
        return False
        