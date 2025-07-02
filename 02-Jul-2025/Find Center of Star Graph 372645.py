# Problem: Find Center of Star Graph - https://leetcode.com/problems/find-center-of-star-graph/

from collections import defaultdict
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        edges1 = defaultdict(list)
        edges2 = defaultdict(list)
        for edge in edges:
            edges1[edge[0]].append(edge[1])
            edges2[edge[1]].append(edge[0])
        for key, value in edges2.items():
            edges1[key].extend(value)
        for key, value in edges1.items():
            if len(value) == len(edges):
                return key