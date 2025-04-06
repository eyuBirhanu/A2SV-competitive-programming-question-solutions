# Problem: Segment with Small Sum - https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/A

n, s = list(map(int, input().split()))
nums = list(map(int, input().split()))
max_len = 0
sum_ = 0
j = 0 
for i in range(len(nums)):
    sum_ += nums[i]
    if sum_ <= s:
        max_len = max(max_len, i-j+1)
    else:
        while sum_ > s:
            sum_ -= nums[j]
            j += 1
            max_len = max(max_len, i-j+1)
print(max_len)
    
        