# Problem: Best Time to Buy and Sell Stock - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy = prices[0]
        for i in range(1, len(prices)):
            profit = prices[i] - buy
            max_profit = max(max_profit, profit)
            buy = min(prices[i], buy)
        return max_profit