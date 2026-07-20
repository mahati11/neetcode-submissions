class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0 
        buy =  0
        n = len(prices)
        m = max(prices)
        if n == 1:
            return 0 
        while buy < n:
            sell = buy + 1
            if prices[buy] == m:
                buy+=1
                continue
            while buy < sell and sell < n :
                if prices[buy] < prices[sell]:
                    profit = max(profit, prices[sell] - prices[buy])
                sell +=1
            buy+= 1
            
        return profit
