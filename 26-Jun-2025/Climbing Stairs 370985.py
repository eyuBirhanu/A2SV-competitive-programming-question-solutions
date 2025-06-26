# Problem: Climbing Stairs - https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        store= {}
        
        def check(i):
            if i > n:
                return 0
            if i == n:
                return 1
            if i in store:
                return store[i]

            store[i] = check(i+1) + check(i+2)
            return store[i]
        return check(0)