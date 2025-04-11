# Problem: Kefa and Company - https://codeforces.com/problemset/problem/580/B

len_, money_diff = list(map(int, input().split()))
friends = []
for _ in range(len_):
    friend = list(map(int, input().split()))
    friends.append(friend)
friends.sort()
max_friendship = 0
friend_val = 0
j = 0
for i in range(len(friends)):
    friend_val += friends[i][1]
    
    if friends[i][0] - friends[j][0] >= money_diff:
        while j < i and friends[i][0] - friends[j][0] >= money_diff:
            friend_val -= friends[j][1]
            j += 1
    max_friendship = max(max_friendship, friend_val)
print(max_friendship)
