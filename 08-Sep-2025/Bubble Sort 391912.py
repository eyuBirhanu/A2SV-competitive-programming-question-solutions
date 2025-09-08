# Problem: Bubble Sort - https://www.hackerrank.com/challenges/ctci-bubble-sort/problem

def countSwaps(a):
    cnt = 0
    for j in range(len(a)):
        for i in range(len(a)-1):
            if a[i] > a[i+1]:
                a[i] ,a[i+1] = a[i+1], a[i]
                cnt += 1
    print(f'Array is sorted in {cnt} swaps.') 
    print(f'First Element: {a[0]}')
    print(f'Last Element: {a[-1]}')