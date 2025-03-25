# Problem: C - Barking Password - https://codeforces.com/gym/588094/problem/C

goal = input()
n = int(input())
comps = []
def check(x,y):
  return x == goal or y == goal or (x[1] == goal[0] and y[0] == goal[1])

for _ in range(n):
  comps.append(input())

ans = "NO"
for i in range(n):
  for j in range(n):
    if check(comps[i],comps[j]):
      ans = "YES"
print(ans)