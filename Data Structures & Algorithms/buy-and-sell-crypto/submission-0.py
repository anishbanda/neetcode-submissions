class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bestBuy = float('inf')
        bestSell = 0
        for price in prices:
            bestBuy = min(price, bestBuy)
            bestSell = max(bestSell, price - bestBuy)
        
        return bestSell
