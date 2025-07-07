# Problem: Operations on Graph - https://www.eolymp.com/en/contests/9060/problems/78602

import sys 
from collections import defaultdict

v = int(sys.stdin.readline())
graph = defaultdict(list)

n = int(sys.stdin.readline())
for i in range(n):
    adj = list(sys.stdin.readline().split())
    if adj[0] == '1':
        graph[adj[1]].append(adj[2])  
        graph[adj[2]].append(adj[1])  
    elif adj[0] == '2':
        print(' '.join(graph[adj[1]]))
