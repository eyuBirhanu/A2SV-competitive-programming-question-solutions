# Problem: B. Ehab Is an Odd Person - https://codeforces.com/problemset/problem/1174/B

len_ = int(input())
nums = list(map(int, input().split()))
if all(x%2 ==0 for x in nums):
    print(' '.join(map(str, nums)))
elif all(x%2 ==1 for x in nums):
    print(' '.join(map(str, nums)))
else:
    nums.sort()
    print(' '.join(map(str, nums)))
