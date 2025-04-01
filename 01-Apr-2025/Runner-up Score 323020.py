# Problem: Runner-up Score - https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    arr_1 = arr[-1]
    for i in range(len(arr))[::-1]:
        if arr[i] != arr_1:
            print(arr[i])
            break