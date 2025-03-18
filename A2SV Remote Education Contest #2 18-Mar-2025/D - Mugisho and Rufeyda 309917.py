# Problem: D - Mugisho and Rufeyda - https://codeforces.com/gym/586622/problem/D

inputs = list(map(int, input().split()))
n = inputs[0]
t = inputs[1]

if n == 1:
    if t == 10:
        print(-1)
    else:
        print(t)
else:
    for i in range(10 ** (n-1), 10 **n):
        if i % t == 0:
            print(i)
            break
    else:
        print(-1)