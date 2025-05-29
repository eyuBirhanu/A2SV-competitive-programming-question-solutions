# Problem: Program to calculate value of nCr using Recursion - https://www.geeksforgeeks.org/program-to-calculate-value-of-ncr-using-recursion/

def nCr(n, r):
    def factorial(num):
        if num == 1:
            return 1
        return num * (factorial(num-1))
    
    N = factorial(n)
    R = factorial(r)
    nR = factorial(n-r)
    value = N// (R * nR)
    return value


if __name__ == "__main__":
    n = 10
    r = 5
    print(int(nCr(n, r)))