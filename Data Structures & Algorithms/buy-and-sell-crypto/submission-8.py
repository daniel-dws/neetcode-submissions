class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0 
        for stock in prices[1:]:
            profit = max(profit, stock - buy)
            buy = min(stock, buy)
        return profit

