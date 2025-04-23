# Problem: Richest Customer Wealth - https://leetcode.com/problems/richest-customer-wealth/description/

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxWealth = 0
        customer = len(accounts)
        bank = len(accounts[0])
        for i in range(customer):
            wealth = 0
            for j in range(bank):
                wealth += accounts[i][j]
            maxWealth = max(maxWealth, wealth)
        return maxWealth
        