# Problem: From adjacency list to adjacency matrix - https://basecamp.eolymp.com/en/problems/3982

import sys
n = int(sys.stdin.readline())
for i in range(n):
    line = ['0' for j in range(n)]
    nums = list(map(int, sys.stdin.readline().split()))
    if nums[0] != 0:
        m = nums[1:]
        for nu in m:
            line[nu-1] = '1'
    print(' '.join(line))