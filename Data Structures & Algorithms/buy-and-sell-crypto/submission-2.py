class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        l,r = 0,1
        while l<len(prices) and r<len(prices):
            if prices[l]<prices[r]:
                profit = prices[r]-prices[l]
                res = max(profit,res)
                r+=1
            else:
                l=r
                r+=1
        return res