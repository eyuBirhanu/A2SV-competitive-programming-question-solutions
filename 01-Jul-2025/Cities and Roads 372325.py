# Problem: Cities and Roads - https://www.eolymp.com/en/contests/9060/problems/78597

import sys
n = int(sys.stdin.readline())
cnt = 0
for i in range(n):
    line = list(map(int, input().split()))
    for j in range(n):
        if line[j] == 1:
            cnt += 1
print(cnt//2)