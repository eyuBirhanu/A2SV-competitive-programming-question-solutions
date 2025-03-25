# Problem: C - Sura loves coding - https://codeforces.com/gym/586622/problem/C

n = int(input())
encode = str(input())
decode = encode[0]
for i in range(1, n):
    if n % 2 and i % 2 or not (n % 2) and not (i % 2):
        decode = encode[i] + decode
    else:
        decode = decode + encode[i]            
print(decode)