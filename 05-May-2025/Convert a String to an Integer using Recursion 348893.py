# Problem: Convert a String to an Integer using Recursion - https://www.geeksforgeeks.org/convert-a-string-to-an-integer-using-recursion/

str_ = '50'
i = len(str_)-1

def convert(s, i):
    return int(s) * 10  ** ((len(str_)-1)-int(i))

def run(i):
    if i < 0:
        return 0
    
    res = 0
    res += convert(str_[i], i)
    
    return res + run(i-1)

print(run(i))

    
