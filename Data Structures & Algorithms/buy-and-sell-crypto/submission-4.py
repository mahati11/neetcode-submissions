class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0 
        buy =  0
        sell = 1
        n = len(prices)
        
        if n == 1:
            return 0 

        while sell < n:
            if prices[buy] < prices[sell]:
                profit = max(profit, prices[sell] - prices[buy])
            else:
                buy = sell
            sell+= 1
            
        return profit
