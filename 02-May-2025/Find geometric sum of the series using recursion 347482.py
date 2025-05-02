# Problem: Find geometric sum of the series using recursion - https://www.geeksforgeeks.org/find-geometric-sum-of-the-series-using-recursion/

def geoSum(n):
    if n == 0:
        return 1
    res = 0
    res += 1 / 3 ** n + geoSum(n-1)
    return res
