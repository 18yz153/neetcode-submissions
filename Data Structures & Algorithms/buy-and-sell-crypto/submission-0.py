class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        lowestbuy = prices[0]
        for i in range(1,len(prices)):
            p = prices[i]-lowestbuy
            profit = max(p,profit)
            if prices[i]< lowestbuy:
                lowestbuy =  prices[i]
        return profit