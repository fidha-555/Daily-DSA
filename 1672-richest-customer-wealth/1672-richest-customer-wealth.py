class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        richest = 0
        for customer in accounts:
            total = sum(customer)
            richest = max(richest,total)
        return richest 
