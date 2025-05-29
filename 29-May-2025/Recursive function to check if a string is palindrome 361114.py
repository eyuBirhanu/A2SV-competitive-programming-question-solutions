# Problem: Recursive function to check if a string is palindrome - https://www.geeksforgeeks.org/recursive-function-check-string-palindrome/

def checkPalendrom(s):
    l = 0
    r = len(s)-1
    def helper(s, l, r):
        if r < l:
            return True
        if s[l] != s[r]:
            return False
        return helper(s, l+1, r-1)
        
    return helper(s, l, r)


if __name__ == "__main__":
    s = "abba"
    print(bool(checkPalendrom(s)))