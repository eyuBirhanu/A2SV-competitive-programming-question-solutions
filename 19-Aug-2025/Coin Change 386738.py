# Problem: Coin Change - https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        
        def dp(remain):
            if remain == 0:
                return 0
            if remain < 0:
                return -1
            
            if remain in memo:
                return memo[remain]
            
            memo[remain] = float('inf')
            for coin in coins:
                res = dp(remain-coin)
                if res != -1:
                    memo[remain] = min(res+1, memo[remain])
            if memo[remain] == float('inf'):
                return -1
            
            return memo[remain]
        
        return dp(amount)