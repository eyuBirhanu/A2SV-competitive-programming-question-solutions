# Problem: Less or Equal - https://codeforces.com/problemset/problem/977/C

input_ = input().split()
inputs = list(map(int, input_)) 
numbers  = input().split() 
nums = list(map(int, numbers))

k = inputs[1]
n = inputs[0]
nums.sort()

ans = 0

if k == 0:
    if nums[0] > 1:
        print(nums[0] -1)
    else:
        print(-1)
else:
    num = nums[k-1]
    cnt = 0
    for i in nums:
        if i <= num:
            cnt += 1
    if cnt == k:
        print(num)
    else:
        print(-1)
