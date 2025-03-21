# Problem: Books - https://codeforces.com/contest/279/problem/B

inputs = list(map(int, (input().split())))
books = list(map(int, (input().split())))

total_time = inputs[1]
len_ = inputs[0]

max_read = 0
sum_ = 0
j = 0

for i in range(len_):
    sum_ += books[i]
    if sum_ <= total_time:
        max_read = max(max_read, (i+1)-j)
    elif sum_ > total_time:
        while j < i and sum_ > total_time:
            sum_ -= books[j]
            j += 1
            if sum_ <= total_time:
                max_read = max(max_read, (i+1)-j)
print(max_read)