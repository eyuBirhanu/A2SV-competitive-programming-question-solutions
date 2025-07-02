# Problem: Sources and sinks - https://basecamp.eolymp.com/en/problems/3986

import sys 
n = int(sys.stdin.readline())
sources = set()
sinks = set()
for i in range(n):
    line = list(map(int, sys.stdin.readline().split()))
    for j in range(len(line)):
        if line[j] == 1:
            sources.add(i+1)
            sinks.add(j+1)
res_sources = [] 
res_sinks = [] 
for i in range(n):
    if i+1 not in sources and i+1 not in sinks:
        res_sources.append(f'{i+1}')
        res_sinks.append(f'{i+1}')
    elif i+1 in sources and i+1 not in sinks:
        res_sources.append(f'{i+1}')
    elif i+1 in sinks and i+1 not in sources:
        res_sinks.append(f'{i+1}')
print(f'{len(res_sources)}',' '.join(res_sources))
print(f'{len(res_sinks)}',' '.join(res_sinks))
