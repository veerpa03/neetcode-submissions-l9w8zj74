class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res =  0
        b,s=0,1
        while s<len(prices) and b<len(prices):
            if prices[b]<prices[s]:
                profit  = prices[s]-prices[b]
                res = max(profit,res)
                s+=1
            else:
                b=s
                s+=1
        return res