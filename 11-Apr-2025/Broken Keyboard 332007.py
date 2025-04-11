# Problem: Broken Keyboard - https://codeforces.com/problemset/problem/1251/A

len_ = int(input())
for _ in range(len_):
    arr = input()
    if len(arr) == 1:
        print(arr)
        continue
    working = set()
    i = 0
    while i < len(arr)-1:
        if arr[i] != arr[i+1]:
            working.add(arr[i])
            i += 1
        elif arr[i] == arr[i+1]:
            i += 2
    if i < len(arr):
        working.add(arr[i])
    res = ''.join(sorted(list(working)))
    print(res)
