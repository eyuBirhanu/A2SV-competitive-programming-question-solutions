# Problem: From Adjacency Matrix to Adjacency List - https://www.eolymp.com/en/contests/9060/problems/78603

import sys
from collections import defaultdict

n = int(sys.stdin.readline())
graph = defaultdict(list)

for i in range(n):
    line = list(map(int, sys.stdin.readline().split()))
    graph[i+1] = []
    for j in range(len(line)):
        if line[j] == 1:
            graph[i+1].append(j+1)

for key, value in graph.items():
    print(f'{len(value)}', ' '.join(f'{i}' for i in value))
