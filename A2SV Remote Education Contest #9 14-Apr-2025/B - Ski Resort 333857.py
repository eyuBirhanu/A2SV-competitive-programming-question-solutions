# Problem: B - Ski Resort - https://codeforces.com/gym/603156/problem/B

len_ = int(input())
for _ in range(len_):
    n, k, q = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    ways = 0
    cnt = 0
    i = 0
    while i < len(nums):
        if nums[i] <= q:
            cnt += 1
        elif nums[i] > q:
            if cnt >= k:
                ways += ((cnt-k+1)*(cnt-k+2)) // 2
            cnt = 0
        i += 1
    if cnt >= k:
        ways += ((cnt - k + 1) * (cnt - k + 2)) // 2

    print(ways)