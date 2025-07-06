# Problem: Find if Path Exists in Graph - https://leetcode.com/problems/find-if-path-exists-in-graph/

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        stack = [source]
        visited = set([source])

        while stack:
            node = stack.pop()
            if node == destination:
                return True
            

            for adj in graph[node]:
                if adj not in visited:
                    stack.append(adj)
                    visited.add(adj)

        return False
        
        
        
        