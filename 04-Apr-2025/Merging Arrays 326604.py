# Problem: Merging Arrays - https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/A

len_a, len_b = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
i = 0
j = 0
ans = []
while i < len(a) and j < len(b):
    if a[i] <= b[j]:
        ans.append(str(a[i]))
        i += 1
    elif b[j] <= a[i]:
        ans.append(str(b[j]))
        j += 1
if i < len(a):
    for k in range(i, len(a)):
        ans.append(str(a[k]))
if j < len(b):
    for k in range(j, len(b)):
        ans.append(str(b[k]))
print(' '.join(ans))