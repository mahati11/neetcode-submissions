class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if sorted(prices) == prices:
            return prices[-1] - prices[0]
        if sorted(prices) == prices[::-1]:
            return 0
        
        diff = []
        for i in range(n-1):
            diff.append(prices[i+1]-prices[i])
        
        m = 0
        for i in diff:
            if i > 0:
                m+=i
        
        return m
