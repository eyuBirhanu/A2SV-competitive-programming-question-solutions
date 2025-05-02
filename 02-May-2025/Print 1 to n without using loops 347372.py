# Problem: Print 1 to n without using loops - https://www.geeksforgeeks.org/print-1-to-n-without-using-loops/

class Solution:
    def printTillN(self, N):
        if N > 0:
            self.printTillN(N-1)
            print(N, end=' ')