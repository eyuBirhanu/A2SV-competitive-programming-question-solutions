# Problem: Alternating Subsequence - https://codeforces.com/contest/1343/problem/C

def check(n):
    if n > 0:
        return 1
    else:
        return -1
    
len_ = int(input())
for _ in range(len_):
    l = int(input())
    nums = list(map(int ,input().split()))
    res = 0
    currSign = check(nums[0])
    currMax = nums[0]
    for n in nums:
        if check(n) == currSign:
            currMax = max(n, currMax)
        else:
            res += currMax
            currSign = check(n)
            currMax = n
    if currMax != 0:
        res += currMax
    print(res)
    
    