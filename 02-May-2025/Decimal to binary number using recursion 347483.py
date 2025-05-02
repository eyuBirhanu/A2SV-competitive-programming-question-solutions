# Problem: Decimal to binary number using recursion - https://www.geeksforgeeks.org/decimal-binary-number-using-recursion/

def toBin(n):
    if n == 1:
        return '1'
    res = ''
        
    res += toBin(n//2) + str(n%2)
    return res