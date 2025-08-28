# Problem: B - Frog 2 - https://atcoder.jp/contests/dp/tasks/dp_b

N, K = map(int, input().split())
h = list(map(int, input().split()))
dp = [0] + [float('inf')] * (N-1)
for i in range(1, N):
    min_cost = float('inf')
    for j in range(1, min(K, i) + 1):
        cost = dp[i-j] + abs(h[i] - h[i-j])
        if cost < min_cost:
            min_cost = cost
    dp[i] = min_cost
print(dp[-1])