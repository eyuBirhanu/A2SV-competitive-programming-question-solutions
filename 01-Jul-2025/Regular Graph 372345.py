# Problem: Regular Graph - https://basecamp.eolymp.com/en/problems/5076

from collections import defaultdict
import sys 
graph = defaultdict(int)
n, m = list(map(int, sys.stdin.readline().split()))
for i in range(m):
    s, e = list(map(int, sys.stdin.readline().split()))
    graph[e] += 1
    graph[s] += 1
cnt = 0
edgeCnt = 0
for i in range(1, n+1):

    if cnt == 0:
        edgeCnt = graph[i]
        cnt += 1
        continue
    if edgeCnt != graph[i]:
        print("NO")
        break
else:
    print('YES')