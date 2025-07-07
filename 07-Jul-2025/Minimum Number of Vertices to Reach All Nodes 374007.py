# Problem: Minimum Number of Vertices to Reach All Nodes - https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        res = []

        graph = defaultdict(list)
        haveIn = set()

        for u, v in edges:
            graph[u].append(v)
            haveIn.add(v) 

        for i in range(n):
            if i not in haveIn:
                res.append(i)
        return res