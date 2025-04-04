# Problem: Sereja and Dima - https://codeforces.com/problemset/problem/381/A

len_ = int(input())
nums = list(map(int, input().split()))
a, b = 0, 0 
i = 0
j = len(nums)-1
cnt = 0
while i < j:
    if nums[i] > nums[j]:
        a += nums[i]
        i += 1
        cnt += 1
    else:
        a += nums[j]
        j -= 1
        cnt += 1
        
        
    if nums[i] > nums[j]:
        b += nums[i]
        i += 1
        cnt += 1
    else:
        b += nums[j]
        j -= 1
        cnt += 1
if cnt < len(nums):
    a += nums[i]
print(a, b)      
